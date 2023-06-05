import discord
import os
import requests
import json
import random
import database_control

client = discord.Client()
command_call = "!"
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encouragements = ["Cheer up!", "Hang in there.", "You are great person!"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("{}ping".format(command_call)):
        await message.channel.send("!ping")

    if msg.startswith("{}inspire".format(command_call)):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_encouragements + database_control.get_encouragements()
    print(options)
    if msg.startswith("!new-enc"):
        print(msg.split("!new-enc ", 1)[1])

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv("BOT_SECRET_TOKEN"))
