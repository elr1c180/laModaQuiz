from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def begin() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Регистрация", callback_data="start_form")
    kb.button(text="Подписаться на Lamoda Tech", url="https://t.me/+l28IFPsVKHsxYzRi")
    kb.adjust(2)
    return kb.as_markup()

def start_quiz() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Запустить Product Quiz", callback_data="start_quiz")
    kb.adjust(2)
    return kb.as_markup()

