from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def final_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Telegram-канал Lamoda Tech", url="https://t.me/+l28IFPsVKHsxYzRi")
    kb.button(text="Команда продукта", url="https://latech.ru/product")
    kb.button(text="Вакансии", url="https://job.lamoda.ru/vacancies")
    kb.adjust(1)
    return kb.as_markup()


