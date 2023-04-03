import random

from aiogram import types
from create_bot import dp
from aiogram.types import Message
import config



@dp.message_handler(commands=['начать', 'start'])

async def mes_start(message: Message):

    await message.answer(text=f'{message.from_user.first_name}, привет\n'
                                f'Сегодня мы с тобой поиграем в интересную игру\n'
                              f'Правила следующие:\n'
                              f'На столе лежат конфеты,\n'
                              f'брать конфеты со стола будем по очереди \n'
                              f'победит тот,\n'
                              f'кто заберет последние конфеты\n'
                              f'для старта напиши: /new \n')



@dp.message_handler(commands=['new'])
async def mes_new_game(message: Message):
    name = message.from_user.first_name
    for geme in config.games:
        if message.from_user.id == geme:
            await message.answer(f'{name} ты уже играешь, напиши количество конфет')
            break
    else:
        config.total = 150
        await message.answer(text=f'Итак, на столе лежит {config.total} конфет\n'
                                    f'Кинем жребий, чей первый ход')
        coin = random.randint(0, 1)



        config.games[message.from_user.id] = 150
        if coin:
            await message.answer(text=f'{message.from_user.first_name}, поздравляю, выпал орел,\n'
                                    f'ты ходишь первый, \n'
                                    f'бери конфеты: от 1 до 28 штук \n'
                                    f'за один ход')

        else:
            await message.answer(text=f'{message.from_user.first_name}, ну вот, искуственный интеллект победил,\n'
                                    f'выпала решка,мой бот ходит первым,\n'
                                    f'а тебе повезет в другой раз,\n'
                                    f'но это не точно')
            await boy_turn(message)

@dp.message_handler()
async def all_catch(message: Message):
    if message.text.isdigit():
        if 0 < int(message.text) <29:
            await player_turn(message)
        else:
            await message.answer(text=f'Ах ты хитрюга! {message.from_user.first_name}\n'
                                      f'Конфет нужно брать хотя бы одну, но не бошьше  28!!!\n'
                                      f'Давай попробуй еще разок')
    else:
        await message.answer(text=" Введи цифрами количество конфет от 1 до 28 ")
async def player_turn(message: Message):
        take_amount = int(message.text)
        print(config.games.get(message.from_user.id))
        config.games[message.from_user.id] = config.games.get(message.from_user.id)-take_amount
        name = message.from_user.first_name
        await message.answer(text=f'{name}, у тебя {take_amount} конфет \n'
                              f'и на столе осталось {config.games.get(message.from_user.id)}')
        if await check_victory(message, name):
            return
        await message.answer(text=f'теперь передаем ход боту')
        await boy_turn(message)
async def boy_turn(message: Message):
        take_amount = 0
        current_total = config.games.get(message.from_user.id)
        if current_total <= 28:
            take_amount = current_total
        else:
            take_amount = current_total%29 if current_total%29 != 0 else 1

        config.games[message.from_user.id] = config.games.get(message.from_user.id)-take_amount
        name = message.from_user.first_name
        await message.answer(text=f'бот взял {take_amount} конфет \n'
                              f'и на столе осталось {config.games.get(message.from_user.id)}')
        if await check_victory(message, 'БОТ'):
            return
        await message.answer(text=f'{name} , теперь твой черёд! \n'
                                  f'Бери конфеты')
async def check_victory(message: Message, name: str):
    if config.games.get(message.from_user.id) <= 0:
        await message.answer(text=f'Победил {name}! \n'
                                  f'это была славная игра \n'
                                  f'сыграй еще раз'
                                  f'нажми: /new')
        config.games.pop(message.from_user.id)
        return True
    else:
        return False