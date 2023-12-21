from aiogram.fsm.state import StatesGroup, State
from handlers import bot_messages

class StepsForm(StatesGroup):
    GET_FIO = State()
    GET_CHEH = State()
    GET_PODRASDELENIE = State()
    GET_PROBLEMA = State()
    GET_PHOTO = State()
    GET_vibor = State()