import discord
from discord import app_commands
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.unknown, name="In Wartungen"))



async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Status(bot))