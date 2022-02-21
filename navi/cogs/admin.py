from discord.ext import commands

from navi.cogs_list import COGS_LIST


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def disconnect(self, ctx):
        """Disconnects the bot"""
        await ctx.send("Disconnecting. Goodbye!")
        await self.bot.close()

    @commands.command()
    async def reload(self, ctx):
        """Reloads the bot"""
        for cog in COGS_LIST:
            self.bot.reload_extension(f"navi.cogs.{cog}")
        print("commands reloaded")


def setup(bot):
    bot.add_cog(Admin(bot))
