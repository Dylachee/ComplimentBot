import json
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Загрузить данные из файла JSON
with open('compliments.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Получить список комплиментов
compliments = data['compliments']

# Создать экземпляр бота
bot = Bot(token="6134936077:AAFU73VCKd8DYS4pv-8kmtLtT1vk2AK5K-A")
dispatcher = Dispatcher(bot)

# Создать клавиатуру с кнопкой "Отправить комплимент"
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton('Отправить комплимент')
keyboard.add(button)

# Обработчик команды /start
@dispatcher.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Отправить приветственное сообщение с клавиатурой
    await message.reply("Привет! Я бот комплиментов. Меня создал Улук что бы поднять тебе настроение. Нажми кнопку 'Отправить комплимент', чтобы получить случайный комплимент.", reply_markup=keyboard)

# Обработчик нажатия на кнопку "Отправить комплимент"
@dispatcher.message_handler(lambda message: message.text == 'Отправить комплимент')
async def send_random_compliment(message: types.Message):
    # Получить случайный комплимент
    random_compliment = random.choice(compliments)
    
    # Отправить комплимент пользователю
    await message.reply(random_compliment)

# Запустить бота
executor.start_polling(dispatcher)
