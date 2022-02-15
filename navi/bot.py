import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command(name="disconnect")
async def disconnect(ctx):
    """Disconnects the bot"""
    await ctx.send("Disconnecting. Goodbye!")
    await bot.close()


@bot.command()
async def reload(ctx):
    """Reloads the bot"""
    bot.reload_extension("navi.cogs.weather")
    print("commands reloaded")


def start():
    bot.load_extension("navi.cogs.weather")
    bot.run(os.getenv("DISCORD_KEY"))
