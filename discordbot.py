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
async def Hey guys(ctx):
    await ctx.send('We have a gift for you')
    
@bot.command()
async def 地雷(ctx):
    await ctx.send('自己紹介❓')
    
@bot.command()
async def 運営(ctx):
    await ctx.send('あほ')
    
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

@bot.command()
async def 香水(ctx):
    await ctx.send('この道具は現在使えません。')
    

    
bot.run(token)
