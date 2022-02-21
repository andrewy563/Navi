import os

import requests
from discord.ext import commands


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, *, location=None):
        """Returns the current weather (default is San Jose)"""
        if not location:
            location = "San Jose"
        r = requests.get(
            "http://api.weatherapi.com/v1/current.json",
            params={"key": os.getenv("WEATHER_KEY"), "q": location},
        )
        if r.status_code == requests.codes.bad_request:
            return await ctx.send("Location does not exist.")
        weather = r.json()
        return await ctx.send(
            (
                f"Weather in {weather.get('location').get('name')}: "
                f"{weather.get('current').get('temp_f')} degrees Fahrenheit\n"
                f"Powered by https://WeatherAPI.com/"
            )
        )


def setup(bot):
    bot.add_cog(Weather(bot))
