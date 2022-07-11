from email import message
from uuid import uuid1
import discord
import random
import asyncio
from config import config
from discord.ext import commands

client = commands.Bot(command_prefix=config.command_prefix)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def auth(ctx):
        answer = random.choice(range(10000,99999))
        role = discord.utils.get(ctx.guild.roles, name=config.role_neme)
        embed = discord.Embed(title="認証用パスワードを生成しました。" + "\n" + str(answer), description=ctx.author.mention + "\n" + "パスワードを認証してください。", color=0xe4ff14)
        await ctx.send(embed=embed)
        Nope = discord.Embed(title="コマンドを再実行してください" + "\n", description=ctx.author.mention + "\n" + "codeが一致しませんでした", color=0xe4ff14)
        authok = discord.Embed(title="認証を完了しました。", description=ctx.author.mention + "に" + "認証済ロールを付与しました。", color=0xe4ff14)
        timeout = discord.Embed(title="コマンドを再実行してください" + "\n", description=ctx.author.mention + "\n" + "120秒以内に認証できませんでした。", color=0xe4ff14)
        def answercheck(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel and m.content.isdigit()

        try:
            waitresp = await client.wait_for('message', timeout=config.timeuot, check=answercheck)
        except asyncio.TimeoutError:
            await ctx.send(embed=timeout)
        else:
                if waitresp.content == str(answer):
                    await ctx.send(embed=authok)
                    await ctx.author.add_roles(role)
                else:
                    await ctx.send(embed=Nope)

client.run(config.discord_token)