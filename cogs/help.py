import discord

from discord import Embed, Member
from typing import Optional
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f'Invalid Command Used, {ctx.author.mention} Udah Salah DiPerbaiki Dong?')    

    @commands.group(name='help', invoke_without_command=True)
    async def helpserver(self, ctx, target: Optional[Member]):
        target = target or ctx.author
        channel = ctx.message.channel
        help = discord.Embed(
            title='__***COMMANDS***__',
            description='__***List Of Commands***___',
            colour=discord.Colour.blue()
        )
        help.set_thumbnail(url='https://i.imgur.com/3odNvba.jpg')
        help.set_author(name='|༺HyperGames༻|', icon_url=target.avatar_url)
        help.set_footer(text='This Bot On Progress Makes Commands (Command Music On This Time Not Working)')
        help.set_image(url="https://images-ext-2.discordapp.net/external/COl0mZHjPwdVXFoxenrUPy1jbX8atqOai7dIO42wMns/https/media.discordapp.net/attachments/709369821439197237/709374347340677231/lineee.gif")
        help.add_field(name='__***Prefix***__', value='***hy!(command)***', inline=True)
        help.add_field(name='__***Commands***__', value='***Moderation***, ***Fun***', inline=True)
        help.add_field(name="__***Example***__", value="***hy!help mod***",inline=True)
        help.add_field(name='__***List Mod***__', value='***Ban***, ***Unban***, ***Kick***, ***Mute***, ***Unmute***, ***Move***', inline=False)
        help.add_field(name='__***List Fun***__', value='***Echo***, ***Clear***, ***Ping***, ***Avatar***', inline=True)
        help.add_field(name='__***List Music***__', value='***Play***, ***Stop***, ***Pause***, ***Resume***, ***Queue***, ***Loop***', inline=False)

        print("Command Help Used By : " + target.name)
        await ctx.send(embed=help)

    '''
    @helpserver.command(name='mod')
    async def moderation(self, ctx):
        author = ctx.message.author

        moderation = discord.Embed(
            colour=discord.Colour.blurple()
        )
        moderation.set_thumbnail(url='https://i.imgur.com/3odNvba.jpg')
        moderation.set_author(name='|༺HyperGames༻|', url='https://i.imgur.com/3odNvba.jpg')
        moderation.add_field(name='The Commands On Moderation Are :', value='Kick, Ban, Unban, Mute, Unmute, Move', inline=False)
        moderation.add_field(name='Note If Your Are Not Moderation', value='Try To Not Make A Problem', inline=True)

        await author.send(embed=moderation)
        await ctx.send("The Commands Sending On {} Dm".format(ctx.author.mention))

    #Commands Fun
    @helpserver.command(name='fun')
    async def for_fun(self, ctx):
        author = ctx.message.author

        fun = discord.Embed(
            colour=discord.Colour.blur()
        )
        fun.set_thumbnail(url='https://i.imgur.com/3odNvba.jpg')
        fun.set_author(name='|༺HyperGames༻|', url='https://i.imgur.com/3odNvba.jpg')
        fun.add_field(name='The Commands On Fun Are :', value='Ping, Clear, Join, Leave', inline=False)
        fun.add_field(name='Note If Your Are Try To Spam Join-Leave Bot', value='-------', inline=True)
        
        await author.send(embed=fun)
        await ctx.send("The Commands Sending On {} Dm".format(ctx.author.mention))

    #Commands Music
    @helpserver.command(name='music')
    async def music_command(self, ctx):
        author = ctx.message.author

        music = discord.Embed(
            colour=discord.Colour.blurple()
        )
        music.set_thumbnail(url='https://i.imgur.com/3odNvba.jpg')
        music.set_author(name='|༺HyperGames༻|', url='https://i.imgur.com/3odNvba.jpg')
        music.add_field(name='The Commands On Music Are :', value='Play, Stop, Pause, Resume, Queue', inline=False)
        music.add_field(name='Note', value='if You Want To Play Music First Join The Bot, And Then hg!play (linkyt)', inline=True)
        
        await author.send(embed=music)
        await ctx.send("The Commands Sending On {} Dm".format(ctx.author.mention))
    '''       

def setup(bot):
    bot.add_cog(Help(bot))     
