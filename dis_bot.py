import discord

import random
import sqlite3
from tabulate import tabulate
from discord.ext import commands
from bot_logic import *

conn = sqlite3.connect('Discord.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
conn.commit()

a = 2

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for guild in client.guilds:#т.к. бот для одного сервера, то и цикл выводит один сервер
        print(guild.id)#вывод id сервера
        for member in guild.members:#цикл, обрабатывающий список участников
            cursor.execute(f"SELECT id FROM users where id={member.id}")#проверка, существует ли участник в БД
            if cursor.fetchone()==None:#Если не существует
                cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 50000, 'S','[]',1,0)")#вводит все данные об участнике в БД
            else:#если существует
                pass
            conn.commit()#применение изменений в БД

@client.event
async def on_member_join(member):
    cursor.execute(f"SELECT id FROM users where id={member.id}")#все также, существует ли участник в БД
    if cursor.fetchone()==None:#Если не существует
        cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 50000, 'S','[]',0,0)")#вводит все данные об участнике в БД
    else:#Если существует
        pass

@client.event
async def on_message(message):
    if len(message.content) > 5:#за каждое сообщение длиной > 10 символов...
        for row in cursor.execute(f"SELECT xp,lvl,money FROM users where id={message.author.id}"):
            expi=row[0]+random.randint(5, 40)#к опыту добавляется случайное число
            cursor.execute(f'UPDATE users SET xp={expi} where id={message.author.id}')
            if row[1] != 0:
                lvch=expi/(row[1]*150)
                print(int(lvch))
                lv=int(lvch)
            if row[1] < lv:#если текущий уровень меньше уровня, который был рассчитан формулой выше,...
                await message.channel.send(f'{message.author.name} - получил новый уровень!')#то появляется уведомление...
                bal=1000*lv
                cursor.execute(f'UPDATE users SET lvl={lv},money={bal} where id={message.author.id}')#и участник получает деньги
    await client.process_commands(message)#Далее это будет необходимо для ctx команд
    conn.commit()

@client.command()
async def acc(ctx): #команда _account (где "_", ваш префикс указаный в начале)
    table=[["Nickname:","money:","lvl:","xp:"]]
    for row in cursor.execute(f"SELECT Nickname,money,lvl,xp FROM users where id={ctx.author.id}"):
        table.append([row[0],row[1],row[2],row[3]])
        await ctx.send(f">\n{tabulate(table)}")

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
