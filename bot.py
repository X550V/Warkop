import discord
import os
import random
import asyncio

from itertools import cycle
from discord.ext import commands, tasks
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='hy!')
client.remove_command('help')
token = "NTU3MjI3NzEyMTM0MTE5NDM0.Xxf3HA.4cagqqdpD4uFq3eIDorn-ecCg4M"

status = cycle(['hy!help','r/help','hg!help','AkuGanteng'])

@client.event
async def on_ready():
    change_status.start()
    print('Logged As')
    print(client.user.name)
    print('-----------')
    

@tasks.loop(seconds=10)    
async def change_status():
     await client.change_presence(activity=discord.Game(next(status))) 
   
#Ping
@client.command()
async def ping(ctx):
    channel = ctx.message.channel
    
    ping = discord.Embed(
        title="PING LATENCY", 
        description=f"Ping: {round(client.latency * 1000)}ms!",
        colour=discord.Colour.purple()
        )
    ping.add_field(name='Name', value=f'{client.mention}', inline=True)

    await ctx.send(embed=ping)
        

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')    

client.run(os.environ['token'])