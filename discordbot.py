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
async def 11月1日(ctx):
    await ctx.send('カミナさん誕生日おめでとう^-^')
    
@bot.command()
async def WaRa(ctx):
    await ctx.send('＃透明床の音ォ～')
    
@bot.command()
async def 裏世界なう(ctx):
    await ctx.send('どこのmap?')
    
@bot.command()
async def 裏世界行く人(ctx):
    await ctx.send('ノ')

@bot.command()
async def カミナさん(ctx):
    await ctx.send('いつもありがと～♪~♪ d(⌒o⌒)b♪~♪')
    
    
@bot.command()
async def お疲れ様でした(ctx):
    await ctx.send('また参加してね(*￣▽￣)ﾉ~~')

bot.run(token)
