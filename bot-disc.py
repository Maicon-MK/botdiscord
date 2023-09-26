import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
my_secret = os.environ['TOKEN_DISCOTD']


@bot.command()
async def inverse(ctx, message):
  await ctx.send(message[::-1])


bot.run(my_secret)
