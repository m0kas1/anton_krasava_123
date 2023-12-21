import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram import Router
from handlers import bot_messages
from utils.stateforms import StepsForm
from handlers import user_messages
from authentication import bot_token

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=bot_token.TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.message.register(bot_messages.get_start, Command(commands='form'))
    dp.message.register(bot_messages.get_FIO, StepsForm.GET_FIO)
    dp.message.register(bot_messages.get_CHEH, StepsForm.GET_CHEH)
    dp.message.register(bot_messages.get_PODRASDELENIE, StepsForm.GET_PODRASDELENIE)
    dp.message.register(bot_messages.get_PROBLEMA, StepsForm.GET_PROBLEMA)
    dp.message.register(bot_messages.get_PHOTO, StepsForm.GET_PHOTO)
    dp.message.register(bot_messages.get_VIBER, StepsForm.GET_vibor)
    dp.include_routers(
        bot_messages.router,
        # user_messages.router
    )
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.run(main())