import os
import discord
from discord.ext import tasks, commands 
import datetime
import time
import asyncio
from uit_calendar import Calendar_util


TOKEN = open("/home/adrian/projects/discord_info/garbagetoken").readline() 
GUILD =  'karantenejobbing'
HELG = 746320599734943744
SCHEDULE = 746008830638424211
client = commands.Bot(command_prefix="$")




@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    #await client.change_presence(activity=discord.Game('Overwatch'))

    await client.change_presence(activity=discord.Streaming(name='Ass and titties', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'))
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


async def send_message():
    await client.wait_until_ready()
    courses = ["INF-2900-1", "INF-2310-1", "INF-1400-1", "MAT-2300-1", "MAT-1002-1", "FIL-0700-1", "BED-2017-1"]
    url = "https://timeplan.uit.no/calendar.ics?sem=21v"
    for course in courses:
        url += f"&module[]={course}"
    cu = Calendar_util(url)
    cu.create_events()
    lectures = cu.get_next_lecture(60*60*24)
    print("Entered loop") 
    sent = 0    
    while not client.is_closed(): 
        now = datetime.datetime.now()
        timestamp = int(datetime.datetime.now().timestamp())
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
        
        elif clock == "23:59:00" and weekday <= 4:
            cu = Calendar_util(url)
            cu.create_events()
            lectures = cu.get_next_lecture(60*60*24)
        else:
            next_lecture = cu.get_next_upcoming_lecture()
            for i, nl in enumerate(next_lecture):
                channel = client.get_channel(id=SCHEDULE)   
                if nl.timestamp - timestamp <= 60*15 and not sent:
                    msg = f"@everyone\n Garbage man here, lecture in {nl.name} is coming up within 15 min"
                    await channel.send(msg)
                if i+1 == len(next_lecture):
                    sent = 1
                elif now.minute >= 15:
                    sent = 0
                    

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
