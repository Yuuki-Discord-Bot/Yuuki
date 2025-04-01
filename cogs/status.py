import discord
from discord import app_commands
from discord.ext import commands, tasks
from asyncio import sleep


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.status.start()
    
    @tasks.loop(seconds=30)
    async def status(self):
        await self.bot.wait_until_ready()
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.unknown, name=f"IN WARTUNGEN"))

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Status(bot))