import discord 
import os

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(guild_ids=[1320613385825681458])
async def hello(ctx):
    await ctx.respond("Hello!")


token = os.getenv('DISCORD_TOKEN')
bot.run(token)
