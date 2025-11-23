from aiogram import F, Router,types
import asyncio
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext


from  Main_Gemini import Promt,Model

import app.keyboard as kb

Model_= Model
chat= Promt

router=Router()


class WaitingMessage(StatesGroup):
    CaptureMessages = State()
    NonCaptureMessages = State()

@router.message(CommandStart())
async def start(message: Message,state: FSMContext):
    await message.answer(f'Привет {message.from_user.first_name}\n ',reply_markup=kb.Start)


@router.message(F.text=="🤖 Начать чат с Gemini 🤖")
async def new_chat(message:types.Message,state:FSMContext):
    await state.set_state(WaitingMessage.CaptureMessages)
    await message.answer('Чат успешно создан✅')

@router.message(WaitingMessage.CaptureMessages)
async def bot_answer(message:types.Message,state:FSMContext):
    if message.text:
        if message.text=='Stop⛔':
            await message.answer('Чат остановлен ✅')
            await state.set_state(WaitingMessage.NonCaptureMessages)
            await message.answer(f'Чтобы запустить чат еще раз нажмите на кнопку ',reply_markup=kb.Start)
        else:
            wait_answer= await message.answer('Генерация текста...⌛')
            question=message.text
            response=chat.send_message(question,
                                       safety_settings={
                                           'HATE': 'BLOCK_NONE',
                                           'HARASSMENT': 'BLOCK_NONE',
                                           'SEXUAL': 'BLOCK_NONE',
                                           'DANGEROUS': 'BLOCK_NONE'
                                       })
            await message.bot.delete_message(chat_id=message.chat.id,message_id=wait_answer.message_id)

            Text=response.text
            if len(Text)>4096:
                for i in range(0,len(Text),4096):
                    await message.answer(Text[i:i+4096])

            else:
                await message.answer(Text,reply_markup=kb.Stop)








