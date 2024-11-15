import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from buttns import menu  # Assuming this file contains button layout

API_TOKEN = '7684404279:AAGE133qvhQX5wA1zML7TwkN36PHtHumU1M'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Salom! Keling, Tosh, Qaychi, Qog`oz o`yinini o`ynaymiz. "
        "Quyidagi variantlardan birini tanlang:",
        reply_markup=menu  # Assuming menu is a predefined button layout
    )


@dp.message_handler(lambda message: message.text not in ["🪨 Tosh", "✂️ Qaychi", "📄 Qog`oz"])
async def invalid_choice(message: types.Message):
    await message.reply(
        "Iltimos, faqat to'g'ri variantlardan birini tanlang: "
        "🪨 Tosh, ✂️ Qaychi yoki 📄 Qog`oz.",
        reply_markup=menu
    )


@dp.message_handler(lambda message: message.text in ["🪨 Tosh", "✂️ Qaychi", "📄 Qog`oz"])
async def game(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(["🪨 Tosh", "✂️ Qaychi", "📄 Qog`oz"])

    # Determine the result
    if user_choice == bot_choice:
        result = "Durrang!"  # Draw
    elif (user_choice == "🪨 Tosh" and bot_choice == "✂️ Qaychi") or \
         (user_choice == "✂️ Qaychi" and bot_choice == "📄 Qog`oz") or \
         (user_choice == "📄 Qog`oz" and bot_choice == "🪨 Tosh"):
        result = "Siz yutingiz!"  # Win
    else:
        result = "Siz yutqazdingiz!"  # Loss

    # Send the result message
    await message.reply(
        f"Sizning tanlovingiz: {user_choice}\nBotning tanlovi: {bot_choice}\nNatija: {result}",
        reply_markup=menu  # Show the menu again after the game
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
