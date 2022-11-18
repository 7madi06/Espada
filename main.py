import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTA0MzE1NDQ4NDA0MzQ2ODgyMA.Ggd6NX.zBa1ZxyUx3KeRHxUJsxeGuN1LgvmPo3rAsBgRs')