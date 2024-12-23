import discord
from discord.ext import commands
from discord import slash_command
import config

class HelloCogs(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @slash_command(
        name="hello",
        description='実行すると hello と出力します',
        guild_ids=config.guild_ids,
    )
    async def hello(self, ctx: discord.ApplicationContext):
        print("send 'Hello!'")
        await ctx.respond("Hello!")

def setup(bot: commands.Bot):
    bot.add_cog(HelloCogs(bot))
