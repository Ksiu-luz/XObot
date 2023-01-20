# from print_tab import return_tab as rt
# from check import check
# import discord
# from discord.ext import commands
# import json
# import asyncio
#
# file_for_config = open('config.json', 'r')
# config = json.load(file_for_config)
#
# intents = discord.Intents.default()
# intents.members = True
# intents.message_content = True
#
# bot = commands.Bot(config['prefix'], intents=intents)
#
#
# @bot.event
# async def on_massage(message):
#     if message.author != bot.user:
#         if message.content == 'игра':
#             await message.channel.send("Ну давай поиграем!")
#             await message.channel.send(rt(tab))
#             await message.channel.send(f"Куда поставим {config['symbol']}? ")
#             return
#         if message.content.isdigit():
#             player_answer = int(message)
#         else:
#             await message.channel.send("Некорректный ввод. Вы уверены, что ввели число?")
#             return
#         if 9 >= player_answer >= 1:
#             if str(tab[player_answer - 1]) not in "XO":
#                 tab[player_answer - 1] = config['symbol']
#                 await message.channel.send(rt(tab))
#                 if config['symbol'] == 'X':
#                     config['symbol'] = 'O'
#                 else:
#                     config['symbol'] = 'X'
#                 tmp = check(tab)
#                 if tmp:
#                     await message.channel.send(tmp, "выиграл!")
#                     is_end = True
#                 elif not (tab[0].isgigit() or tab[1].isgigit() or tab[2].isgigit() or tab[3].isgigit()
#                           or tab[4].isgigit() or tab[5].isgigit() or tab[6].isgigit() or tab[7].isgigit()
#                           or tab[8].isgigit()):
#                     message.channel.send("Ничья!")
#                     is_end = True
#                 else:
#                     await message.channel.send(f"Куда поставим {config['symbol']}? ")
#                     return
#                 if is_end:
#                     await message.channel.send("Итоговая таблица:")
#                     await message.channel.send(rt(tab))
#                     config['symbol'] = 'X'
#                     raise SystemExit
#             else:
#                 await message.channel.send("Эта клеточка уже занята")
#                 return
#         else:
#             await message.channel.send("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
#             return
#
#
# @bot.event
# async def on_ready():
#     print('BOT ONLINE')
#
#
# async def main():
#     await bot.start(config['token'])
#
#
# if __name__ == '__main__':
#     is_end = False
#     tab = list(range(1, 20))
#     asyncio.run(main())
#     while not is_end:
#         pass
#     else:
#         tab = list(range(1, 20))
#         raise SystemExit


import discord
from discord.ext import commands
import json
from print_tab import return_tab as rt
from check import check


file_for_config = open('config.json', 'r')
config = json.load(file_for_config)

intents = discord.Intents.default()
intents.message_content = True  # intents for read messages
intents.members = True  # intents for get list

bot = commands.Bot(intents=intents, command_prefix=config['prefix'])


@bot.event
async def on_ready():
    print('BOT ONLINE')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    global tab
    if message.content.lower() == 'игра':
        config['symbol'] = 'X'
        tab = list(range(1, 20))
        await message.channel.send("Ну давай поиграем!")

        await message.channel.send(rt(tab))
        await message.channel.send(f"Куда поставим {config['symbol']}? ")
        return
    try:
         player_answer = int(message.content)
    except:
        await message.channel.send("Некорректный ввод. Вы уверены, что ввели число?")
        return
    if 9 >= player_answer >= 1:
        if str(tab[player_answer - 1]) not in "XO":
            tab[player_answer - 1] = config['symbol']
            await message.channel.send(rt(tab))
            if config['symbol'] == 'X':
                config['symbol'] = 'O'
            else:
                config['symbol'] = 'X'
            tmp = check(tab)
            if tmp:
                await message.channel.send(f"{tmp} выиграл!")
                is_end = True
            elif not (type(tab[0]) == int or type(tab[1]) == int or type(tab[2]) == int or type(tab[3]) == int
                      or type(tab[4]) == int or type(tab[5]) == int or type(tab[6]) == int or type(tab[7]) == int
                      or type(tab[8]) == int):
                await message.channel.send("Ничья!")
                is_end = True
            else:
                await message.channel.send(f"Куда поставим {config['symbol']}? ")
                return
            if is_end:
                await message.channel.send("Итоговая таблица:")
                await message.channel.send(rt(tab))
                return
        else:
            await message.channel.send("Эта клеточка уже занята")
            return
    else:
        await message.channel.send("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
        return


tab = list(range(1, 20))
bot.run(config['token'])
