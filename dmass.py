import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time
from random import choice, randint

client = commands.Bot(command_prefix = 'wr!', case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print('Logged in')
    print('--------')
    print('--------')
    print('CREATED AND HOSTED BY INVADER OP')


    @client.command()
    async def hello(ctx):
        await ctx.send(f"{choice(('Hello','Hai', 'Hi', 'Hey', 'Hiya'))} {ctx.author.mention}!")
        

    
    @commands.has_permissions(administrator=True)
    @client.command(pass_context = True)
    async def send(ctx, *, content: str):
            for member in ctx.message.server.members:
                try:
                    await client.send_message(member, content)
                    await client.say("DM Sent".format(member))
                except:
                    print("can't")
                    await client.say("DM can't Sent")


client.run("NzIwNjkzMDM5OTUzMDg0NDI3.XuJrsg.y9Kl1XO-5Rv5zpAxTrswmx8itdk")                
