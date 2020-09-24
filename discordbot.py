from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def WaRa(ctx):
    await ctx.send('即死')
    
@bot.command()
async def ソルセルト(ctx):
    await ctx.send('tintin')
    
@bot.command()
async def しなめす(ctx):
    await ctx.send('その香水のせいだよ～♪')
    
@bot.command()
async def 筋肉マン(ctx):
    await ctx.send('令和であります。')
    
bot.run(token)
