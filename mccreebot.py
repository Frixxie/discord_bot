import os
import discord
from discord.ext import tasks, commands 
import datetime
import asyncio


TOKEN = open("/home/adrian/projects/mccreebottoken").readline() 
GUILD =  'Team Avatar'
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    await client.change_presence(activity=discord.Game('Overwatch'))

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


async def send_message():
    await client.wait_until_ready()
    print("Entered loop") 
    while not client.is_closed(): 
        now = datetime.datetime.now()
        clock = str(datetime.time(now.hour, now.minute))
        if clock == "12:00":
            print("It's "+str(now.hour)+":"+str(now.minute))
            txt = "It's High Noon!!!"
            channel = client.get_channel(id=785975501470695505)   
            await channel.send(txt,file=discord.File('highnoon.jpg'))
            await asyncio.sleep(120)
        else:
            await asyncio.sleep(15)
            continue

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    #message starts with hi or hello then print these
    if message.content.startswith('Is it High Noon?') or message.content.startswith('high noon?') or message.content.startswith('highnoon?'):
        await message.channel.send('Its High Noon somewhere in the world {0.author.mention} '.format(message))

client.loop.create_task(send_message())
client.run(TOKEN)
