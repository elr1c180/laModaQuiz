import asyncio
from aiogram import Bot, Dispatcher
from handlers import start, form_start, quiz_start
from database import init_db

# Запуск бота
async def main():
    bot = Bot(token="7266872684:AAH2NTvCA_uPCnaDq70kkWisrxIXDko03MU")
    dp = Dispatcher()

    dp.include_routers(start.router, form_start.router, quiz_start.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    init_db()
    asyncio.run(main())
