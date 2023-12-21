# from aiogram import Router, F
# from aiogram.types import CallbackQuery, Message
# from keyboards import inline
#
#
# router = Router()
# global g
#
# @router.callback_query(F.data == 'АО «ЮМЭК»')
# async def send_random_value(callback: CallbackQuery):
#     g = callback.message.answer('АО «ЮМЭК»')
#
# @router.callback_query(F.data == 'ООО «МЗВА-ЧЭМЗ»')
# async def send_random_value(callback: CallbackQuery):
#     g = callback.message.answer('ООО «МЗВА-ЧЭМЗ»')
#
# @router.callback_query(F.data == 'ООО «ИНСТА»')
# async def send_random_value(callback: CallbackQuery):
#     g = callback.message.answer('ООО «ИНСТА»')
#
# @router.callback_query(F.data == 'ООО «Энерготрансизолятор»')
# async def send_random_value(callback: CallbackQuery):
#     g = callback.message.answer('ООО «Энерготрансизолятор»')
#
# @router.callback_query(F.data == 'ООО «ВОЛЬТА»')
# async def send_random_value(callback: CallbackQuery):
#     g = callback.message.answer('ООО «ВОЛЬТА»')
#
# @router.callback_query(F.data == 'ООО «ФОРЭНЕРГО-ИНЖИНИРИНГ»')
# async def send_random_value(callback: CallbackQuery):
#     g = callback.message.answer('ООО «ФОРЭНЕРГО-ИНЖИНИРИНГ»')