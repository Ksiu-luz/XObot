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
