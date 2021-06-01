# beer30bot2.py, the new and improved bot!
# 1. Notifies users it's beer:30 with command to jockey music bot to play
#the lego beer song on youtube
# 2. Gives n randomly selected breweries to try via OpenBreweryDB
# 3. Congratulates a user whenever they do something awesome(may come later.)
# "m!play https://www.youtube.com/watch?v=ATBl4qH9I54"

import os
import discord
from discord.ext import commands, tasks
from discord.utils import get
#import aiocron
from art import text2art
from datetime import datetime
import openbrewerydb
from time import localtime, strftime

# TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')
# CHANNEL_ID2 = 'aux-cord'
CHANNEL_ID1 = 'general'

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    tm = strftime("%I:%M %p", localtime())
    print("Beer30Bot2 is online.")
    print(tm)

# @aiocron.crontab('59 15 * * *')
# async def beer_30():
#     channel = bot.get_channel(CHANNEL_ID1)
#     await channel.send("Ahem, testing!")

@bot.event
async def beer_30(ctx):
    tm = strftime("%H:%M", localtime())
    if tm == "16:30":
        print("It's that time!")
        await ctx.channel.send("It's Beer:30!")

@bot.command(
    help='Uses some tools to create an ascii clock display.',
    brief='Tells the user the current time in ascii display.'
)
async def popatop(ctx):
    tm = strftime("%I:%M %p", localtime())
    tmstr = str(tm)
    tmart = text2art(tmstr)
    await ctx.channel.send("`%s`" %(tmart))

@bot.command(
    help='Uses some tools to create an ascii word display.',
    brief='Returns the desired word to the user in ascii display.'
)
async def beerme(ctx, input):
    art = text2art(input)
    await ctx.channel.send("`%s`" %(art))

@bot.command(
    help='Uses some tools to pull n randomly selected beers from OpenBreweryDB.',
    brief='Returns n amount of randomly selected beers from OpenBreweryDB as\n brewery information to the user. Use the syntax `!recmeone n city state`.\n If a state or city has two words, put them inside `''`.'
)
async def recmeone(ctx, n: int, city, state):
    #await ctx.channel.send("Wish I could, but I don't have that feature yet.")
    
    ct = city.lower()
    st = state.lower()
    
    data = openbrewerydb.load(city=ct, state=st)
    useful_data = data.drop(data.columns[[0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17]], axis=1)
    
    if n < 1:
        await ctx.channel.send("Haha, sorry, but we don't serve under age users.")
    elif n > len(data):
        await ctx.channel.send("Ouch! Looks like there isn't enough for you to try in %s, %s!" % (city, state))
    # elif ct not in data:
    #     await ctx.channel.send("It doesn't look like that place is in the database. Try somewhere else?")
    else:
        sample = useful_data.sample(n)
        await ctx.channel.send("Here are %d breweries to try from %s, %s. Check your local store:" % (n, city, state))
        await ctx.channel.send(sample)

bot.run('insert_your_token_here')
