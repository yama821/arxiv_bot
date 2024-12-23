import discord 
import os

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True # ?

    bot = discord.Bot(intents=intents)

    bot.load_extension("Cogs.hello")

    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)
