#This just keeps your bot alive.
#Use with UptimeRobot

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "OwO, What's this?"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target = run)
  t.start()
