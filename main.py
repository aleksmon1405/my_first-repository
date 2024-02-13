from aiogram import Bot, Dispatcher, F
import random
from aiogram.filters import CommandStart
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)


BOT_TOKEN = '6981317449:AAEjtdXrYE4Nk6bwjUCeGz91oKikf-oM7As'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

f = open('files\\first.txt', 'r', encoding='UTF-8')
zodiac = f.read().split('\n')
f.close()

# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='♈ Овен ♈',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='♉ Телец ♉',
    callback_data='big_button_2_pressed'
)

big_button_3 = InlineKeyboardButton(
    text='♊ Близнецы ♊',
    callback_data='big_button_3_pressed'
)

big_button_4 = InlineKeyboardButton(
    text='♋ Рак ♋',
    callback_data='big_button_4_pressed'
)

big_button_5 = InlineKeyboardButton(
    text='♌ Лев ♌',
    callback_data='big_button_5_pressed'
)

big_button_6 = InlineKeyboardButton(
    text='♍ Дева ♍',
    callback_data='big_button_6_pressed'
)

big_button_7 = InlineKeyboardButton(
    text='♎ Весы ♎',
    callback_data='big_button_7_pressed'
)

big_button_8 = InlineKeyboardButton(
    text='♏ Скорпион ♏',
    callback_data='big_button_8_pressed'
)

big_button_9 = InlineKeyboardButton(
    text='♐ Стрелец ♐',
    callback_data='big_button_9_pressed'
)

big_button_10 = InlineKeyboardButton(
    text='♑ Козерог ♑',
    callback_data='big_button_10_pressed'
)

big_button_11 = InlineKeyboardButton(
    text='♒ Водолей ♒',
    callback_data='big_button_11_pressed'
)

big_button_12 = InlineKeyboardButton(
    text='♓ Рыбы ♓',
    callback_data='big_button_12_pressed'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2],
                     [big_button_3],
                     [big_button_4],
                     [big_button_5],
                     [big_button_6],
                     [big_button_7],
                     [big_button_8],
                     [big_button_9],
                     [big_button_10],
                     [big_button_11],
                     [big_button_12]])


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Выберите свой знак зодиака!',
        reply_markup=keyboard
    )

#реагирует при отправке юзером 'Привет'
@dp.message()
async def ru_menu(message: Message):
        if message.text =='Привет':
            await message.answer(
                text='Выберите свой знак зодиака!',
                reply_markup=keyboard
            )

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))
   # await callback.message.answer(text='Ура! Нажата кнопка 1')


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_3_pressed'
@dp.callback_query(F.data == 'big_button_3_pressed')
async def process_button_3_press(callback: CallbackQuery):
   await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_4_pressed'
@dp.callback_query(F.data == 'big_button_4_pressed')
async def process_button_4_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_5_pressed'
@dp.callback_query(F.data == 'big_button_5_pressed')
async def process_button_5_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_6_pressed'
@dp.callback_query(F.data == 'big_button_6_pressed')
async def process_button_6_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_7_pressed'
@dp.callback_query(F.data == 'big_button_7_pressed')
async def process_button_7_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_8_pressed'
@dp.callback_query(F.data == 'big_button_8_pressed')
async def process_button_8_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_9_pressed'
@dp.callback_query(F.data == 'big_button_9_pressed')
async def process_button_9_press(callback: CallbackQuery):
   await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_10_pressed'
@dp.callback_query(F.data == 'big_button_10_pressed')
async def process_button_10_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_11_pressed'
@dp.callback_query(F.data == 'big_button_11_pressed')
async def process_button_11_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_12_pressed'
@dp.callback_query(F.data == 'big_button_12_pressed')
async def process_button_12_press(callback: CallbackQuery):
    await callback.message.answer(random.choice(zodiac))

if __name__ == '__main__':
    dp.run_polling(bot)
