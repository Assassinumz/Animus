import aiml
import discord
import asyncio
import random

#--------------TYPE YOUR TOKEN AND OTHER STUFF BELOW--------------#
TOKEN = "" # your token

channel_name = "animus" # default channel name

colour = 0xffb7c5 # default colour for embeds
#-----------------------------------------------------------------#

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

    if "https://" in message.content.lower() or "www." in message.content.lower():
        return

    if message.content == "<@547321575993769984>":
        msg = "Hey There, I'm a Animus an AIML Chatbot made for discord\nType `;help` for more info"
        await channel.send(msg)
        return

    elif message.content.lower() == ";help":
        embed = discord.Embed(title="Help", description="List of commands", colour=colour)
        embed.add_field(name=";help", value="Shows this help message")
        embed.add_field(name=";info", value="Shows information about the bot")
        embed.add_field(name=";invite", value="Provides the invite link for the bot and support server")
        await channel.send(embed=embed)
        
    else:
        response = kernel.respond(message.content)
        await asyncio.sleep(random.randint(0,2))
        await channel.send(response)

client.run(TOKEN)