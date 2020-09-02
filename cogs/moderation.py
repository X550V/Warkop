import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Moving Channel
    @commands.command()
    async def move(self, ctx, member: discord.Member):
        await member.edit(voice_channel=None)
        await ctx.message.delete()
        print("Command Move Used By : " + member.name)

    #Dm Server
    @commands.command()
    async def send(self, ctx, *, args=None):
        if args != None:
            members = ctx.guild.members
            for member in members:
                try:
                    await member.send(args)
                    print("'" + args + "' sent to: " + member.name)

                except:
                    print("Couldn't send '" + args + "' to: " + member.name)

        else:
            await ctx.channel.send("Ga bisa Yah Ga bisalah.....")                

    #Kick Members
    @commands.command()
    @has_permissions(manage_roles=True, kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Good Bye {member.mention}, Has Been Killed By {ctx.author.mention}')
        print("Command Kick Used By : " + member.name)

    @kick.error
    async def kick_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            await bot.send_message("Sorry {}, you do not have permissions to do that!".format(ctx.message.author))

    #Ban Members
    @commands.command()
    @has_permissions(manage_roles=True, ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Good Bye {member.mention}, Has Been Eliminated By {ctx.author.mention}')
        print("Command Ban Used By : " + member.name)

    @ban.error
    async def ban_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            await ctx.send_message("Sorry {}, you do not have permissions to do that!".format(ctx.message.author))    

    #Unban
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                print("Command Unban Used By : " + member.name)
                return

    #Mute Members
    @commands.command(pass_context=True)
    async def mute(self, ctx, member : discord.Member=None):
        role = discord.utils.get(ctx.guild.roles,name='Muted')
        if not member:
            await ctx.send("Please Specify A Member")
            return
        await member.add_roles(role)
        await ctx.send(f"Hey Your Teammate {member.mention} Has Been Slain An Enemy!")
        print("Command Mute Used By : " + member.name)

    #Unmute Members
    @commands.command(pass_context=True)
    async def unmute(self, ctx, member : discord.Member=None):
        role = discord.utils.get(ctx.guild.roles,name='Muted')
        if not member:
            await ctx.send("Please Specify A Member")
            return
        await member.remove_roles(role)
        await ctx.send(f"Hey Your Teammate {member.mention} Has Been Kill By Enemy!")
        print("Command Unmute Used By : " + member.name)

def setup(bot):
    bot.add_cog(Moderation(bot))     
