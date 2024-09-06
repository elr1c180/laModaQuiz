from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove,  CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database import add_user
from fsm import form


from kb.begin import start_quiz

router = Router()
@router.callback_query(F.data == 'start_form')  
async def start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Как тебя зовут?\n\nНапиши в поле ввода сообщения Имя и Фамилию")
    await state.set_state(form.Form.name)

# Обрабатываем имя и фамилию
@router.message(form.Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Где ты работаешь?\n\nНапиши в поле ввода сообщения Компанию и должность")
    await state.set_state(form.Form.work)

# Обрабатываем компанию и должность
@router.message(form.Form.work)
async def process_work(message: Message, state: FSMContext):
    await state.update_data(work=message.text)
    await message.answer("И последний шаг – добавь адрес почты для связи:")
    await state.set_state(form.Form.email)

@router.message(form.Form.email)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    
    user_data = await state.get_data()
    name = user_data['name']
    work = user_data['work']
    email = user_data['email']
    
    user_data = await state.get_data()
    email = message.text

    if add_user(message.from_user.id, user_data['name'], user_data['work'], email):
        await message.answer("Готово!\nВперед к играм и челленджам 🚀", reply_markup=start_quiz())
        await state.clear()
    else:
        await message.answer("Пользователь уже существует")
    
    # Завершаем FSM
    await state.clear()