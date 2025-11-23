import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router


load_dotenv()
Token = os.getenv("TOKEN")


bot = Bot(token=Token)
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Bot started')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')
