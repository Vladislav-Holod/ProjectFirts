from aiogram.types import  KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup

Start=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🤖 Начать чат с Gemini 🤖')]
    ],resize_keyboard=True

)
Stop=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Stop⛔')]
    ],resize_keyboard=True
)
