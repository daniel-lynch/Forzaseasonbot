#!/usr/bin/env python3
import discord
import asyncio
import os
from datetime import datetime, timedelta

seasons = ["Spring", "Summer", "Autumn", "Winter"]

game = os.environ.get('game')

if game == "FH4":
    spring = datetime(2020,12,10,hour=9,minute=30)
if game == "FH5":
    spring = datetime(2021,11,4,hour=9,minute=30)

def getseason():
    today = datetime.now()
    season = int((today - spring).days / 7)
    if season > 3:
        season = season % 4
    return(seasons[season])

client = discord.Client()
loop = client.loop

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    loop.create_task(discord_presence(loop))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!season'):
        season = getseason()
        if season == "Spring":
            await message.channel.send(f":sunflower: The Current Season is {season} :sunflower:")
        if season == "Summer":
            await message.channel.send(f":fire: The Current Season is {season} :fire:")
        if season == "Autumn":
            await message.channel.send(f":fallen_leaf: The Current Season is {season} :fallen_leaf:")
        if season == "Winter":
            await message.channel.send(f":snowflake: The Current Season is {season} :snowflake:")

async def discord_presence(loop):
    game = discord.Game(getseason())
    await client.change_presence(status=discord.Status.online, activity=game)
    await asyncio.sleep(1800)
    loop.create_task(discord_presence(loop))

client.run(os.environ.get('api'))
