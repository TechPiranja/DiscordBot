import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy']
good_words = ['Cheer up!', 'Hang in there!', 'You are a great person!']

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!inspire'):
    await message.channel.send(get_quote())

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(good_words))

keep_alive()
client.run(os.getenv('TOKEN'))
