'''
Бот
'''

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_gb = Bot("6248063014:AAHOTpnqBUz5SizIszDJSPsHaeHieMcwZ-o")
dp =Dispatcher(bot_gb)
async def on_start(_):
    print('Бот готов к работе!')

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton1 = InlineKeyboardButton(text='Молоко', url='https://online.metro-cc.ru/search?q=%D0%BC%D0%BE%D0%BB%D0%BE%D0%BA%D0%BE')
urlButton2 = InlineKeyboardButton(text='Яйца', url='https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca/yayca')
urlButton3 = InlineKeyboardButton(text='Сыр', url='https://online.metro-cc.ru/search?q=%D1%81%D1%8B%D1%80')
urlButton4 = InlineKeyboardButton(text='Колбаса', url='https://online.metro-cc.ru/search?q=%D0%BA%D0%BE%D0%BB%D0%B1%D0%B0%D1%81%D0%B0')
urlButton5 = InlineKeyboardButton(text='Столешница', url='https://leroymerlin.ru/search/?q=%D1%81%D1%82%D0%BE%D0%BB%D0%B5%D1%88%D0%BD%D0%B8%D1%86%D0%B0&suggest=true')
urlButton6 = InlineKeyboardButton(text='Напольная вешалка', url='https://leroymerlin.ru/search/?q=%D0%BD%D0%B0%D0%BF%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%B2%D0%B5%D1%88%D0%B0%D0%BB%D0%BA%D0%B0&suggest=true')
urlButton7 = InlineKeyboardButton(text='Стеллаж', url='https://leroymerlin.ru/search/?q=%D1%81%D1%82%D0%B5%D0%BB%D0%BB%D0%B0%D0%B6&suggest=true')
urlButton8 = InlineKeyboardButton(text='Шкаф', url='https://leroymerlin.ru/search/?q=%D1%88%D0%BA%D0%B0%D1%84&suggest=true')
urlkb.add(urlButton1, urlButton2, urlButton3, urlButton4, urlButton5, urlButton6, urlButton7, urlButton8)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Пожалуйста, помоги"),
            types.KeyboardButton(text="Мне ничего не нужно"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer("Привет! Нужна помощь в выборе магазина в зависимости от товара, который необходимо преобрести?",
                        reply_markup=keyboard)
    print(message)

@dp.message_handler()
async def com_help(message: Message):
    if message.text == "Да! Помоги, пожалуйста":
         await message.answer(
            f'{message.from_user.first_name}, постараюсь!')
         await message.answer('выбери товар:', reply_markup=urlkb)
    elif message.text == 'Нет, мне ничего не нужно':
        await message.answer(f'{message.from_user.first_name}, повезло!')
    print(message)

executor.start_polling(dp, skip_updates=True, on_startup=on_start)


