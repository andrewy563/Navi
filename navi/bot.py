import os

import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("!hello")


@bot.command(name="weather")
async def weather(ctx):
    r = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={"key": os.getenv("WEATHER_KEY"), "q": "San Jose"},
    )
    weather = r.json()
    await ctx.send(
        f"Weather in San Jose: {weather.get('current').get('temp_f')} degrees Fahrenheit"
    )


@bot.command(name="disconnect")
async def disconnect(ctx):
    await ctx.send("Disconnecting. Goodbye!")
    await bot.close()


def start():
    bot.run(os.getenv("DISCORD_KEY"))
