import os
import discord
from discord.ext import tasks, commands 
import datetime
import asyncio


TOKEN = open("/home/adrian/projects/discord_info/garbagetoken").readline() 
GUILD =  'karantenejobbing'
HELG = 746320599734943744
SCHEDULE = ''
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
        weekday = datetime.datetime.today().weekday()
        
        if clock == "12:00:00":
            print("It's "+str(now.hour)+":"+str(now.minute))
            txt = "It's High Noon!!!"
            channel = client.get_channel(id=HELG)   
            await channel.send(txt,file=discord.File('highnoon.jpg'))
            await asyncio.sleep(120)
        
        elif clock == "13:00:00" and weekday <= 4:
            txt = "Snart Helg"
            channel = client.get_channel(id=HELG)   
            await channel.send(txt)
            await asyncio.sleep(120)
        
        elif clock == "13:00:00" and weekday >= 4:
            txt = "HEEEEELG!!!!"
            channel = client.get_channel(id=HELG)   
            await channel.send(txt,file=discord.File('helg.gif'))
            await asyncio.sleep(120)

        else:
            await asyncio.sleep(15)
            continue


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.content.startswith('bad bot') or message.content.startswith('Bad bot'):
        await message.channel.send('Hey I am doing best {0.author.mention} fucking scrub'.format(message))

    elif message.content.startswith('fuck you') or message.content.startswith('screw you'):
        await message.channel.send('Hey I am doing best {0.author.mention} fucking scrub'.format(message))

client.loop.create_task(send_message())
client.run(TOKEN)
