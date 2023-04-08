import discord
from discord.ext import commands
from bot_logic import *

a = 2

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def привет(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Привет!')

@client.command()
async def хелп(ctx):
    await ctx.send('Я бот, да ты и сам знаешь.\n**Мои команды:**\n```!привет - в*ывод сообщения с приветом.``` ```!правила - свод правил сервера.``` ```!хелп - эта команда.``` ```!пароль (кол-во символов) - генератор паролей.``` ```!смайл - получить рандомный смайлик.``` ```!монетка - класическая монетка для твоего спора).``` ```!стата - статистика сервера.```')

@client.command()
async def пароль(ctx, number: int):
    await ctx.send(gen_pass(number))

@client.command()
async def правила(ctx):
    await ctx.send('**Правила сервера:**\n1) Не использовать нецензурные выражения.\n2)Прислушиваться к администрации и модераторам сервера.\n3)Не рекламировать что-либо.')

@client.command()
async def смайл(ctx):
    await ctx.send(smail())

@client.command()
async def монетка(ctx):
    await ctx.send(coin())

@client.command()
async def стата(ctx):
    embed=discord.Embed(title=f"Statystyki serwera {ctx.guild.name}")
    embed.add_field(name="Users:", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Channels:", value=(len(ctx.guild.channels) - a), inline=False)
    await ctx.send(embed=embed)


client.run("Token")
