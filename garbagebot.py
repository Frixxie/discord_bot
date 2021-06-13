import os
import discord
from discord.ext import tasks, commands 
import datetime
import time
import asyncio
import uit_calendar_util
import random

TOKEN = open("/home/fredrik/projects/discord_info/garbagetoken").readline() 
GUILD =  'karantenejobbing'
HELG = 746320599734943744
SCHEDULE = 746008830638424211
client = commands.Bot(command_prefix="$")
bad_responds = ["Hey man I am doing my best {0.author.mention} fucking scrub ", "Let's see if you can do better {0.author.mention} :joy:", "Fuck off {0.author.mention}", "Take a hike on the highway {0.author.mention}", "At least I did something {0.author.mention} you useless trash "]
br_size = len(bad_responds)-1
good_responds = ["Thank you :D ", "I know, I'm the best :sunglasses:","Fine piece of work {0.author.mention}"]
gr_size = len(good_responds)-1


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    #await client.change_presence(activity=discord.Game('Overwatch'))

    await client.change_presence(activity=discord.Streaming(name='Ass and titties', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'))
    print(f'{client.user} is connected to the following guild:\n', f'{guild.name}(id: {guild.id})')


async def send_message(cu):
    await client.wait_until_ready()
    next_lectures = cu.get_next_lecture(60*60*24)
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

        elif clock == "23:59:00":
            cu.update_events()
            next_lectures = cu.get_next_lecture(60*60*24)
 
        elif len(next_lectures) > 0:

            for lecture in next_lectures:
                print(lecture)

            timestamp = int(datetime.datetime.now().timestamp())
            print(str(next_lectures[0].timestamp - timestamp), str(60*15))

            if next_lectures[0].timestamp - timestamp < 60*15:
                channel = client.get_channel(id=SCHEDULE)
                lecture = next_lectures.pop(0)
                msg = f"@everyone Garbage man here, lecture in {lecture.name} is coming up within 15 min"
                await channel.send(msg)
                print("sent lecture notification")

        await asyncio.sleep(1)

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.content.startswith('bad bot') or message.content.startswith('Bad bot') or message.content.startswith('fuck you') or message.content.startswith('screw you'):
        i = random.randint(0,br_size)
        await message.channel.send(bad_responds[i].format(message))
    
    elif message.content.startswith('nice job') or message.content.startswith('good bot') or message.content.startswith('good job') or message.content.startswith('bot good'):
        i = random.randint(0,gr_size)
        await message.channel.send(good_responds[i].format(message))
    
if __name__ == '__main__':
    courses = ["INF-2900-1", "INF-2310-1", "INF-1400-1", "MAT-2300-1", "MAT-1002-1", "FIL-0700-1", "BED-2017-1"]
    url = "https://timeplan.uit.no/calendar.ics?sem=21v"
    cu = uit_calendar_util.Calendar_util(url, courses)
    client.loop.create_task(send_message(cu))
    client.run(TOKEN)
