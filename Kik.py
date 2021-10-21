#This is the Kik functionality of PeriBot
import sys
import os
import contextlib

with contextlib.redirect_stdout(None):
    automatic_setup = os.path.isdir("kik-bot-api-unofficial")
    if automatic_setup == False:
        os.system('git clone -b new https://github.com/GreenBed/kik-bot-api-unofficial')
    os.system('pip3 install ./kik-bot-api-unofficial')
try:
    import kik_unofficial
except ModuleNotFoundError:
    os.system('pip install kik_unofficial')

import kik_unofficial.datatypes.xmpp.chatting as chatting
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.errors import LoginError
from kik_unofficial.datatypes.xmpp.login import ConnectionFailedResponse

global kik_authenticated, client

def kik_login(username, password):
    username = sys.argv[1] if len(sys.argv) > 1 else username
    password = sys.argv[2] if len(sys.argv) > 2 else password

    def main():
        PeriBot()
    global client

    class PeriBot(KikClientCallback):
        global client

        def __init__(self):
            global client
            client = KikClient(self, username, password)

        def on_authenticated(self):
            print("Kik login successful!")
            global kik_authenticated
            kik_authenticated = True

        def on_chat_message_received(self, chat_message: chatting.IncomingChatMessage):
            client.send_chat_message(chat_message.from_jid, "This bot does not have any commands on Kik (yet)!\nCheck me out on Discord, PeriBot#6551")

        def on_connection_failed(self, response: ConnectionFailedResponse):
            print("Kik login failed!")

        def on_login_error(self, login_error: LoginError):
            print("Kik login failed!")

    if __name__ == '__main__':
        main()

def send_kik_message(jid, message_to_send):
    try:
        client.send_chat_message(jid, message_to_send)
        return True
    except:
        return False

def fetch_jid(given_username):
    def get_jid(given_username):
        global client
        try:
            grab_jid = client.get_jid(given_username)
            return grab_jid
        except:
            return False
    jid = get_jid(given_username)
    attempts = 1
    while jid == False:
        if attempts > 5:
            return False
        else:
            jid = get_jid(given_username)
            attempts = attempts + 1
    return jid

kik_authenticated = False
print("logging in to Kik...")
kik_login("PeriBotOfficial", "censored")
while kik_authenticated == False:
        pass

#Do discord bot stuff after this.
