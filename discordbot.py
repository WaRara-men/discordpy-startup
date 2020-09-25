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
async def neko(ctx):
    await ctx.send('にゃーん')
    
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
    
#coding:UTF-8
import discord
from discord.ext import tasks

TOKEN = "NzU3MTk1NTA1ODg0MjAwOTgy.X2c3RA.HFB2h5hyuSmnwuVdzNXUJCMFMAM" #トークン
CHANNEL_ID = 750635752450293793 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

    
bot.run(token)
