from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def first() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="За одно открытие", callback_data="q1_right")
    kb.button(text="За два открытия", callback_data="q1_wrong")
    kb.button(text="За пять открытий", callback_data="q1_wrong")
    kb.adjust(1)

    return kb.as_markup()


def second() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Ваша подборка на сегодня", callback_data="q2_wrong")
    kb.button(text="С чем носить", callback_data="q2_right")
    kb.button(text="Похожие товары", callback_data="q2_wrong")
    kb.adjust(1)
    
    return kb.as_markup()

def third() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="5%", callback_data="q3_wrong")
    kb.button(text="20%", callback_data="q3_right")
    kb.button(text="45%", callback_data="q3_wrong")
    kb.adjust(1)
    
    return kb.as_markup()

def fourth() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="11,1%", callback_data="q4_wrong")
    kb.button(text="29,1%", callback_data="q4_right")
    kb.button(text="37%", callback_data="q4_wrong")
    kb.adjust(1)
    
    return kb.as_markup()

def fifth() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="10млн", callback_data="q5_wrong")
    kb.button(text="20млн", callback_data="q5_right")
    kb.button(text="30млн", callback_data="q5_wrong")
    kb.adjust(1)
    
    return kb.as_markup()