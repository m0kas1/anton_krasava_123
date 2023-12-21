from aiogram import Router, F, Bot
from aiogram.filters.command import Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from keyboards.reply import main, ispravit
from aiogram.fsm.context import FSMContext
from utils.stateforms import StepsForm
from keyboards.inline import inline_kb
# from handlers.user_messages import g
from id import a
import os
import zipfile
from authentication import bot_token

bot = Bot(token=bot_token.TOKEN, parse_mode='HTML')

channel_id = '-1002084616413'

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}!", reply_markup=main)

@router.message(Command("help"))
async def cmd_start(message: Message):
    await message.answer('Список команд:\n/start\n/help')
@router.message()
async def get_start(message: Message, state: FSMContext):
    if message.text.lower() == 'отправить проблему':
        await message.answer('Введите ваше ФИО')
        await state.set_state(StepsForm.GET_FIO)
async def get_FIO(message: Message, state: FSMContext):
    if message.text.count(' ') == 2 and message.text.count(' ') != len(message.text):
        # await message.answer(f'Твоё ФИО: {message.text}')
        await state.update_data(fio=message.text)
        await state.set_state(StepsForm.GET_CHEH)
        # await message.answer('Выберите ваш завод', reply_markup=inline.inline_kb)
        await message.answer('Выберите ваш завод', reply_markup=inline_kb.as_markup())
    else:
        await message.answer('Попробуйте ещё раз')

@router.callback_query(F.data.startswith("«"))
async def get_CHEH(callback: CallbackQuery, state: FSMContext):
    await state.update_data(cheh=callback.data)
    await state.set_state(StepsForm.GET_PODRASDELENIE)
    await callback.message.answer('Введите ваше подразделение:')
# async def get_CHEH(message: Message, state: FSMContext):
#     # await message.answer(f'Ваш СП: {message.text}')
#     await state.update_data(cheh=message.text)
#     await state.set_state(StepsForm.GET_PODRASDELENIE)
#     await message.answer('Введите ваше подразделение:')

async def get_PODRASDELENIE(message: Message, state: FSMContext):
    if message.text == None:
        await message.answer('Введите нормально текст')
    # await message.answer(f'Ваше подразделение: {message.text}')
    else:
        await state.update_data(podraselenit=message.text)
        await state.set_state(StepsForm.GET_PROBLEMA)
        await message.answer('Опишите вашу проблему')

async def get_PROBLEMA(message: Message, state: FSMContext):
    if message.text == None:
        await message.answer('Введите нормально текст')
    else:
        await state.update_data(problema=message.text)
        await state.set_state(StepsForm.GET_PHOTO)
        await message.answer('Отправьте фото. ЕСЛИ ФОТО НЕТ - ВВЕДИТЕ ЛЮБОЙ ТЕКСТ')
async def get_PHOTO(message: Message, state: FSMContext, bot: Bot,):
    global data_user, PHOTO, TEG
    # await state.update_data(photo=message.photo[-1].file_id)
    # await state.set_state(StepsForm.GET_PHOTO)
    c = 0
    while c != 1:
        if message.photo:
            await state.update_data(photo=message.photo[-1].file_id)
            await state.set_state(StepsForm.GET_PHOTO)
            await bot.download(
                message.photo[-1],
                destination=f"img/{message.photo[-1].file_id}.jpg"
            )
            c = 1
        else:
            # d = message.text.lower()
            # if d == 'нет':
            #     c = 1
            #     break
            # else:
            # await message.answer('Введите корректное значение')
            break
    content_data = await state.get_data()
    TEG = f'@{message.from_user.username}'
    d = dict(content_data)
    d['TEG'] = TEG
    print(f'Данные отправителя {d}')
    # print(d['photo'][-1])
    FIO = content_data.get('fio')
    CHEH = content_data.get('cheh')
    PODRASDELENIE = content_data.get('podraselenit')
    PROBLEMA = content_data.get('problema')
    PHOTO = content_data.get('photo')
    data_user = f'Данные пользователя:\r\n' \
                f'ФИО: {FIO}\n' \
                f'СП: {CHEH}\n' \
                f'Подразделение: {PODRASDELENIE}\n' \
                f'Проблема: {PROBLEMA}\n' \
                f'Тег: {TEG}'
    # await message.answer(data_user)
    if PHOTO is None:
        await message.answer(data_user, reply_markup=ispravit)
    else:
        await message.answer_photo(photo=PHOTO, caption=data_user, reply_markup=ispravit)
    await state.update_data(gey=message.text)
    await state.set_state(StepsForm.GET_vibor)

async def get_VIBER(message: Message, state: FSMContext):
    if message.text.lower() == 'исправить':
        await state.clear()
        if os.path.isfile(f'img/{PHOTO}.jpg'):
            os.remove(f'img/{PHOTO}.jpg')

        if os.path.isfile(f'txt/{TEG}.txt'):
            os.remove(f'txt/{TEG}.txt')

        if os.path.isfile(f'zip/{TEG}.zip'):
            os.remove(f'zip/{TEG}.zip')
        # removing_files = glob.glob(f'/img/{PHOTO}.jpg')
        # for i in removing_files:
        #     os.remove(i)
        await message.answer(f"Hello {message.from_user.first_name}!", reply_markup=main)
        # await message.answer(get_start)
    if message.text.lower() == 'отправить':
        await state.clear()
        my_file = open(f"txt/{TEG}.txt", "w+", encoding='utf-8')
        my_file.write(data_user)
        my_file.close()

        file_zip = zipfile.ZipFile(f'zip/{TEG}.zip', 'w')
        file_zip.close()

        file_zip = zipfile.ZipFile(f'zip/{TEG}.zip', 'a')
        file_zip.write(f'txt/{TEG}.txt')
        if os.path.isfile(f'img/{PHOTO}.jpg'):
            file_zip.write(f'img/{PHOTO}.jpg')
        file_zip.close()

        documnet = FSInputFile(path=f'zip/{TEG}.zip')
        await message.answer('Файл отправлен!!!', reply_markup=main)
        # await message.answer_document(document=documnet, caption='Открой меня)')
        await bot.send_document(chat_id=channel_id, document=documnet)
        # await message.copy_to(chat_id=channel_id, caption=j.message_id)

        if os.path.isfile(f'img/{PHOTO}.jpg'):
            os.remove(f'img/{PHOTO}.jpg')

        if os.path.isfile(f'txt/{TEG}.txt'):
            os.remove(f'txt/{TEG}.txt')

        if os.path.isfile(f'zip/{TEG}.zip'):
            os.remove(f'zip/{TEG}.zip')
        # b = {"photo": PHOTO, "caption": data_user}
        # await message.forward_from_message_id()
        # await state.clear()
        # if PHOTO is None:
        #     # await message.answer(chat_id=, text=data_user)
        #     await message.answer(chat_id="6383652769", text=data_user)