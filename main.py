from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

BOT_TOKEN = "7951188300:AAHglCoQpr9FpYTduwOTeVXUo8V2yVnBnaA"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Statistika", callback_data="stats"),
            InlineKeyboardButton(text="⚙️ Sozlamalar", callback_data="settings")
        ],
        [InlineKeyboardButton(text="❓ Yordam", callback_data="help")]
    ])

def back_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")]
    ])

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Xush kelibsiz! Menyudan tanlang:", reply_markup=main_menu())

@dp.callback_query(F.data == "back")
async def back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text("Asosiy menyu:", reply_markup=main_menu())
    await callback.answer()

@dp.callback_query(F.data == "stats")
async def stats_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📊 Statistika:\nFoydalanuvchilar: 1000\nXabarlar: 5000",
        reply_markup=back_menu()
    )
    await callback.answer()

@dp.callback_query(F.data == "settings")
async def settings_handler(callback: types.CallbackQuery):
    settings_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔔 Bildirishnomalar", callback_data="notifications")],
        [InlineKeyboardButton(text="🌐 Til", callback_data="language")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")]
    ])
    await callback.message.edit_text("⚙️ Sozlamalar:", reply_markup=settings_menu)
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())