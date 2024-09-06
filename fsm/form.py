from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    name = State()  
    work = State() 
    email = State() 
