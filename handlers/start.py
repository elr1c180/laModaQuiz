from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, InputFile
from aiogram.types import FSInputFile
from kb.begin import begin
from database import get_all_users
import csv
router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        '''Привет!\n
Добро пожаловать в нашу фэшн-вселенную Lamoda Tech 🌟\n
Что ты найдешь на стенде:\n
▪️ LaBasket – играй в баскетбол кроксами (что? да!)\n
▪️ Гонка доставки – проверь свои знания в фэшн-терминах и помоги нашей курьерской доставке LM Express доставить заказ до пользователя\n
▪️ Product Quiz – логический тренажер с элементами квеста, будет интересно!\n
▪️ VR-примерка: загружай свое фото и испытай на себе шоппинг будущего\n
Давай знакомиться, отгадывать загадки, зарабатывать LaCoins и тратить их на классный мерч 🙂
''',
        parse_mode='html',
        reply_markup=begin()
    )

@router.message(Command("result"))
async def send_results(message: Message):
    # Получаем данные пользователей
    users = get_all_users()
    
    # Создаем CSV-файл
    csv_file = 'results.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Chat ID", "Name", "Work", "Email", "Score"])
        writer.writerows(users)
    
    # Открываем CSV-файл в бинарном режиме и создаем InputFile
    
    document = FSInputFile(csv_file, filename=csv_file)  # Создаем InputFile из файла
    await message.answer_document(document, caption="Here are the results.")