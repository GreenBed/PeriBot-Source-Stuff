#Yeah yeah i know this code is inefficient, i repurposed it from another bot i wrote when i didnt know how to make stuff like this more efficient. Im just lazy. 

import discord
import random
import time

token = "Your token here"
client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  lowercase_message = message.content.lower()
  if lowercase_message == "!coin":
   coin = ("heads", "tails")
   await message.channel.send("Flipping a coin...")
   time.sleep(1)
   await message.channel.send("It landed on " + random.choice(coin) + "!")
  elif lowercase_message.startswith("!roll"):
   try:
    dice_number = lowercase_message.replace('!roll ', '', 1)
    if lowercase_message == '!roll':
     await message.channel.send("To roll a dice, please use `!roll\" [number]`\nExample: `!roll 6`")
    elif lowercase_message == '!roll 0':
     await message.channel.send("You can't have a 0 sided dice, silly goose!")
     time.sleep(1)
     await message.channel.send("Please add a valid number after the roll command.\nExample: \"!roll 6\"")
    elif lowercase_message == '!roll 1':
     await message.channel.send("You can't have a 1 sided dice, silly goose!")
     time.sleep(1)
     await message.channel.send("Please add a valid number after the roll command.\nExample: \"!roll 6\"")
    elif lowercase_message == '!roll 2':
     await message.channel.send(
      "Don't you think \"!coin\" would be a better command to use for that?\nOh well... As you wish, user.")
     await message.channel.send("Violating the laws of physics and rolling a 2 sided dice...")
     time.sleep(1)
     rolled_dice = random.choice(range(1, int(dice_number)))
     await message.channel.send("It landed on " + str(rolled_dice) + "!")
    elif lowercase_message == '!roll [number]':
     await message.channel.send("Put an actual number where it says [number], silly goose!")
    else:
     dice_number = lowercase_message.replace('!roll ', '', 1)
     await message.channel.send("Rolling a " + dice_number + " sided dice...")
     time.sleep(0.5)
     rolled_dice = random.choice(range(1, int(dice_number)))
     await message.channel.send("It landed on " + str(rolled_dice) + "!")
   except ValueError:
     await message.channel.send("Wait a minute, that's not right.\n\"" + dice_number + "\" is not a valid number!\nPlease use a valid number and try again.\nExample: `!roll 6`")
client.run(token)
