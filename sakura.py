import aiml
import discord
import asyncio
import random

TOKEN = "" # your token

channel_name = "sakura" # default channel name

client= discord.Client()

# AIML startup
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

# on_ready
@client.event
async def on_ready():
    print('---------------')
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")

# on_message
@client.event
async def on_message(message):
    channel = message.channel

    if message.author.bot or str(message.channel) != channel_name:
        return
    
    if message.author == client.user:
        return

    if message.content is None:
        return

    if message.content.lower() == ";info":
        msg = "Hey There, I'm a AIML Chatbot made for discord\nType `;help` for more info"
        await client.send_message(channel, msg)

    else:
        response = kernel.respond(message.content)
        await client.send_typing(channel)
        await asyncio.sleep(random.randint(0,2))
        await client.send_message(channel, response)

client.run(TOKEN)