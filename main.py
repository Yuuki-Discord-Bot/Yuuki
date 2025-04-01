import discord, os, json
from discord.ext import commands
from colorama import Fore
from datetime import datetime
import pytz
from dotenv import load_dotenv

load_dotenv()


def current_time():
    return datetime.now(pytz.timezone('Europe/Berlin')).time().strftime("%H:%M:%S")



class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents, help_command = None)
    
    async def on_ready(self):
        await load_cogs()
        cmdsync = await self.tree.sync()
        print(Fore.WHITE + current_time() + " > " + Fore.RESET + f"{self.user.name} ist online! Es wurden {str(len(cmdsync))} Slashcommands syncronisiert und {str(len(self.commands))} Commands. Version 2.0")
        

async def load_cogs():
    for root, dirs, files in os.walk("./cogs"):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                cog_path = os.path.join(root, file).replace(os.sep, '.')[2:-3]
                if not cog_path.endswith("_u"):
                    try:
                        await bot.load_extension(cog_path)
                        print(Fore.WHITE + current_time() + " > " + Fore.GREEN + "[Starting] " + Fore.RESET + f"Loaded {cog_path}")
                    except Exception as e:
                        print(Fore.WHITE + current_time() + " > " + Fore.RED + "[FEHLER!] " + Fore.RESET + f"Failed to load {cog_path}: {e}")

bot = PersistentViewBot()

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
