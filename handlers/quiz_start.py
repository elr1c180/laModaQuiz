from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from fsm import quiz

from database import *

from kb.questions import *
from kb import final


router = Router()

@router.callback_query(F.data == 'start_quiz') 
async def first_q(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "В складской зоне ПВЗ Lamoda есть 3 лампочки, а в коридоре 3 выключателя. За какое минимальное открытие дверей можно определить какой выключатель к какой лампочке относится?",
        reply_markup=first()
    )
    await state.set_state(quiz.Quiz.question1)

@router.callback_query(quiz.Quiz.question1)
async def second_q(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'q1_right':
        await state.update_data(question1=2)
    else:
        await state.update_data(question1=0)

    await callback.message.answer(
        "Как в Lamoda называется функционал на базе нейросетей, который подбирает несколько образов к якорному товару? Ищи подсказку на нашем стенде 🙃",
        reply_markup=second()
    )
    await state.set_state(quiz.Quiz.question2)


@router.callback_query(quiz.Quiz.question2)
async def third_q(callback: CallbackQuery, state: FSMContext):
    print(callback.data)
    if callback.data == 'q2_right':
        await state.update_data(question2=1)
    else:
        await state.update_data(question2=0)

    await callback.message.answer(
        "В  каталоге Lamoda 35% всех футболок серого цвета. А 13% всех товаров составляют футболки, но не серые. Сколько процентов от всех товаров в каталоге составляют футболки?",
        reply_markup=third()
    )
    await state.set_state(quiz.Quiz.question3)

@router.callback_query(quiz.Quiz.question3)
async def fourth_q(callback: CallbackQuery, state: FSMContext):
    print(callback.data)
    if callback.data == 'q3_right':
        await state.update_data(question3=3)
    else:
        await state.update_data(question3=0)

    await callback.message.answer(
        "Рассчитайте Retention Rate на конец года. У компании X было 6 млн постоянных пользователей, за год пришло 4,3 млн новых и ушло 4,25 млн из текущих.",
        reply_markup=fourth()
    )
    await state.set_state(quiz.Quiz.question4)

@router.callback_query(quiz.Quiz.question4)
async def fifth_q(callback: CallbackQuery, state: FSMContext):
    print(callback.data)
    if callback.data == 'q4_right':
        await state.update_data(question4=3)
    else:
        await state.update_data(question4=0)

    await callback.message.answer(
        "Сколько строк исторических данных мы использовали для обучения ML-модели предсказания брака товаров? Ищи подсказку на нашем стенде 🙃",
        reply_markup=fifth()
    )
    await state.set_state(quiz.Quiz.question5)

@router.callback_query(quiz.Quiz.question5)
async def final_q(callback: CallbackQuery, state: FSMContext):
    print(callback.data)
    if callback.data == 'q5_right':
        await state.update_data(question5=1)
    else:
        await state.update_data(question5=0)

    q = await state.get_data()
    print(q)
    x = int(q['question1']) + int(q['question2']) + int(q['question3']) + int(q['question4']) + int(q['question5'])
    score = x
    update_score(callback.from_user.id, score)
    if x <= 4:
        await callback.message.answer(

            f"Ты набрал {x} LaCoins из 10!\nПопытай удачу в LaBasket и Гонке доставки :) ",
        )

    elif x >=5:
        await callback.message.answer(
            f"Ты набрал {x} LaCoins из 10!\nПокажи свой результат на стенде и получи приз :)",
        )

    await callback.message.answer(
        "Останемся на связи!",
        reply_markup=final.final_kb()
    )
    await state.clear()