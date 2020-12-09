import os

import discord
import datetime

now = datetime.datetime.now()
clock = str(datetime.time(now.hour, now.minute, now.second))

TOKEN = open("/home/adrian/projects/mccreebottoken").readline() 
GUILD =  'Team Avatar'
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

"""
@client.event
async def message(message):
    print("nani")
    
    # TODO: Find a way to create a new message on a given time 
    message = discord.Message(state=0,channel=discord.TextChannel,data=None)
    
    if clock == "12:00:00":
        txt = "It's High Noon!!!"
        await message.channel.send(txt)
"""
@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    #message starts with hi or hello then print these
    if message.content.startswith('Hi') or message.content.startswith('Hello'):
        await message.channel.send('Ah hello {0.author.mention} u bitch'.format(message))
    #when the message with help then do this
    elif message.content.startswith('help'):
        await message.channel.send("Git gud")

    elif message.content.startswith('You blastard'):
        await message.channel.send('no but it why')
    elif message.content.startswith('if you go accident what u gonna do'):
        await message.channel.send('WHY YOU FUCK ME I FUCK YOU BLOODY')
        await message.channel.send('Bloody blastard')
    elif message.content.startswith('Bye') or message.content.startswith('Goodbye'):
        await message.channel.send('Bye have a nice day')
    elif message.content.startswith('Man why am I talking to a bot?'):
        await message.channel.send('Cus ur 4everalone #getrekt')


client.run(TOKEN)
