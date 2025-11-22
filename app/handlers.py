from aiogram import F, Router,types
import asyncio
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from  Main_Gemini import start_response

Router=Router()


class MyStates(StatesGroup):
    waiting_response=State()

@Router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}\n Введите 1 чтобы начать')


@Router.message(F.text=='1')
async def response(message: Message,state: FSMContext):
    await message.answer(f'Напишите запрос в gemini')
    await state.set_state(MyStates.waiting_response)

@Router.message(MyStates.waiting_response)
async def response_waiting(message: Message,state: FSMContext):
    if message.text == '2':
        await state.clear()
        await message.answer("Общение завершено. Чтобы начать снова, введите /start или 1.")
    try:
        date = start_response(message.text)
        await message.answer(f"{date}\n\n(Чтобы закончить общение, напишите 2)")
    except Exception as e:
        await message.answer((f"Ошибка при обработке запроса: {str(e)}\n\n(Чтобы закончить — напишите 2)"))






