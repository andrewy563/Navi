import os

from discord.ext import commands
from dotenv import load_dotenv

from navi.cogs_list import COGS_LIST

load_dotenv()

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


def start():
    for cog in COGS_LIST:
        bot.load_extension(f"navi.cogs.{cog}")
    bot.run(os.getenv("DISCORD_KEY"))
