import aiml
import discord
import asyncio
import random

TOKEN = ""
channel_name = "sakura"

client= discord.Client()

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

@client.event
async def on_ready():
    print('---------------')
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")

@client.event
async def on_message(message):
    channel = message.channel

    if message.author.bot or str(message.channel) != channel_name:
        return
    
    if message.author == client.user:
        return

    if message.content is None:
        return

    if message.content == '/info':
        msg = "Hey There, I'm a AIML Chatbot made for discord\nBy: Assassin umz#3274"
        await client.send_message(channel, msg)

    else:
        response = kernel.respond(message.content)
        await asyncio.sleep(random.randint(0,2))
        await client.send_message(channel, response)

client.run(TOKEN)