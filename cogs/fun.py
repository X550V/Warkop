import discord
from random import choice, randint
from discord import Embed, Member
from typing import Optional
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Echo
    @commands.command(name="hello")
    async def say_hello(self, ctx, target: Optional[Member]):
        await ctx.send(f"{choice(('Hello','Hai', 'Hi', 'Hey', 'Hiya'))} {ctx.author.mention}!")
        print("Command Hello Used By : " + Member.name)

    #Clear
    @commands.command(name='purge')
    async def clear(self, ctx, amount: int, target: Optional[Member]):
        target = target or ctx.author
        await ctx.channel.purge(limit=amount + 1)
        print("Command Purge Used By : " + target.name)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Specify An Amount Of Message To Delete!')            
         
    #Showing Avatar
    @commands.command()
    async def avatar(self, ctx, member: discord.Member): 
        show_avatar = discord.Embed(

        color=discord.Color.blue()  
    )
        show_avatar.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=show_avatar)        
        print("Command Avatar Used By : " + member.name)

def setup(bot):
    bot.add_cog(Fun(bot))     
