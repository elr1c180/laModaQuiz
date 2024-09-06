from aiogram.fsm.state import StatesGroup, State

class Quiz(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()