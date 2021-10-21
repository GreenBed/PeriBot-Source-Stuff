import discord
import emoji

token = "Bot token here"
client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  triggers_list = []
  triggers = {}
  lowercase_message = message.content.lower()
  triggers_dictionary = open("triggers.txt", "r+")
  gid = str(message.guild.id)
  group_trigger = str(gid + "//" + lowercase_message)
  for line in triggers_dictionary:
      key, value = line.split()
      key_edit = key.replace("__", " ")
      value_edit = value.replace("__", " ")
      triggers[key_edit] = value_edit
  if group_trigger in triggers:
    step1 = emoji.emojize(triggers[group_trigger])
    response = step1.replace("//linebreak//", "\n")
    await message.channel.send(response)
  if message.author == client.user:
    return
  elif lowercase_message == "!commands":
    await message.channel.send("~COMMANDS~\n`!list` - Group triggers\n`!add` - Add a trigger\n`!delete` - Delete a trigger\n")
  elif lowercase_message.startswith("!delete"):
      if lowercase_message == "!delete":
          await message.channel.send("To delete a trigger, use `!delete [trigger]`\nExample: `!delete uwu`")
      else:
        key = lowercase_message.replace('!delete ', '', 1)
        trigger_to_replace = gid + "//" + key
        await message.channel.send("Attempting to delete \"" + key + "\" from triggers. Say `!list` to view triggers!")
        with open('triggers.txt', 'r') as triggers_file:
            step1 = triggers_file.read()
            step2 = step1.replace(trigger_to_replace, "DELETED//" + trigger_to_replace)
        with open('triggers.txt', 'w') as triggers_file:
            triggers_file.write(step2)
  elif lowercase_message.startswith("!add"):
    try:
        raw = message.content
        key = raw.replace('!add ', '', 1)
        if lowercase_message == "!add":
            await message.channel.send("To add a trigger, use `add [trigger] > [response]`\nExample: `!add uwu > owo`")
        elif key.startswith("!"):
            await message.channel.send("You cannot add a trigger that uses PeriBot's default prefix, which is `!`")
        else:
            reply = key.replace(" > ", "\", I say \"", 1)
            await message.channel.send(emoji.emojize("You say \"" + reply + "\""))
            raw_split = key.split(" > ")
            if len(raw_split) <= 1:
                raise IndexError
            target_trigger = str(raw_split[0])
            lower_trigger = target_trigger.lower()
            final_input = str(lower_trigger) + " > " + str(raw_split[1])
            step1 = final_input.replace(" > ", "!@#$")
            step2 = step1.replace(" ", "__")
            step3 = step2.replace("!@#$", " ")
            step4 = step3.replace("\n", "//linebreak//")
            step5 = str("\n" + gid + "//" + step4)
            step6 = emoji.demojize(step5)
            x = open("triggers.txt", "a")
            x.write(step6)
    except UnicodeEncodeError:
      await message.channel.send("To prevent abuse I will not save special fonts, obscure emojis, or known crash codes. Your trigger was NOT saved!")
    except IndexError:
      await message.channel.send("That appears to be an invalid command, your trigger was not saved. Make sure that you have put \" > \" inbetween your trigger and response!")
  elif lowercase_message == "!list":
    number = len(gid) + 1
    step1 = open("triggers.txt", "r")
    step2 = step1.readlines()
    for string in step2:
        if string.startswith(gid + "//"):
            step3 = string[int(number):]
            step4 = step3.replace("/", ":white_small_square:", 1)
            step5 = step4.split(" ", 1)
            step6 = step5[0]
            step7 = step6.replace("__", " ")
            step8 = step7.replace("//linebreak//", "")
            triggers_list.append(str(step8))
    step9 = str(triggers_list)
    step10 = step9.replace("[", "")
    step11 = step10.replace("]", "")
    step12 = step11.replace(", ", "\n")
    step13 = step12.replace("'", "")
    await message.channel.send("Triggers for this group:\n" + emoji.emojize(step13))
    await message.channel.send("_(Keep in mind that **triggers** are stored as lowercase and **responses** are not.)_")
