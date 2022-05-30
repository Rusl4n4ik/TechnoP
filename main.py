from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard import languages, menubtn, back_m, lang, xizmat
import pathlib
from pathlib import Path
from aiogram.types import ContentType, Message
from fsms import Block, Info, Num, Feedback
from aiogram.dispatcher import FSMContext


API_TOKEN = '5129552109:AAFDehMcyQhuZr-gIvS2QBDNuH4NX0jGpJo'

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=languages)


@dp.callback_query_handler(text='ozb')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Asosiy Menyu:', reply_markup=menubtn)


@dp.message_handler(Text(equals="📞 Murojat uchun"))
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAANQYpNSX3c9w-JENIa72SW_-rdWvl8AAgO9MRs5DZhI7ytHhQ3y_FoBAAMCAAN4AAMkBA',
                            caption="🏥  Zuhal Med klinikasi\n📍 Manzil:  Samarqand tumani, Xo'ja Ahrori Vali Ma'naviyat ko'chasi 18A uy\n\nMurojaat uchun:\n☎️ +998 (55) 702-01-02\n☎️ +998 (55) 702-02-03\n👩🏼‍💻 @zuhalmed_admin"
                            )


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(Text(equals="📍 Bizning manzil"))
async def location(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id=chat_id,longitude=66.938027, latitude=39.671019)
    await message.answer("📍 Manzil:  Samarqand tumani, Xo'ja Ahrori Vali Ma'naviyat ko'chasi 18A uy\n\nMurojaat uchun:\n☎️ +998 (55) 702-01-02\n☎️ +998 (55) 702-02-03\n👩🏼‍💻 @zuhalmed_admin")


@dp.message_handler(Text(equals="✅ Natijalar"))
async def ans(message: types.Message):
    await message.answer("Namunada ko'rsatilgandek ID va Parol ni kiriting. ID bo'sh joy Parol\nNamuna: 12345 ABCD12", reply_markup=back_m)


@dp.message_handler(Text(equals="🚫 Bekor qilish"))
async def back(message: types.Message):
    await message.answer('🔝 Asosiy Menyu', reply_markup=menubtn)


@dp.message_handler(Text(equals="🇺🇿 Tilni o'zgartirish"))
async def back(message: types.Message):
    await message.answer('Tilingizni tanlang:', reply_markup=lang)


@dp.message_handler(Text(equals="🧾 Qabul"))
async def back(message: types.Message):
    await message.answer("Qabulga yozilish uchun kerakli bo'limni tanlang",reply_markup=types.ReplyKeyboardRemove())
    chat_id = message.from_user.id
    await bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAOFYpNhhjZJEzeAwZEkRSqc_S4bNbIAAiG9MRsUVKFISiNdp1O4IYcBAAMCAAN5AAMkBA')
    await Block.bulim.set()


@dp.message_handler(state=Block)
async def bulim(message: types.Message, state: FSMContext):
    text = message.text
    await state.finish()
    print(text)
    await message.answer("Ismingiz va familiyangizni kiriting:")
    await Info.ism_fam.set()


@dp.message_handler(state=Info)
async def bulim(message: types.Message, state: FSMContext):
    text = message.text
    await state.finish()
    print(text)
    await message.answer("Telefon raqamingizni qoldring")
    await Num.telefon.set()


@dp.message_handler(state=Num)
async def bulim(message: types.Message, state: FSMContext):
    text = message.text
    await state.finish()
    print(text)
    await message.answer('Malumot uchun rahmat', reply_markup=back_m)



@dp.message_handler(Text(equals="📝 Fikr mulohaza"))
async def back(message: types.Message):
    await message.answer('📝 Fikr mulohaza')
    await Feedback.ftxt.set()


@dp.message_handler(state=Feedback)
async def feedback(message: types.Message, state: FSMContext):
    text = message.text
    await state.finish()
    print(text)
    await message.answer('Fikr-mulohaza uchun rahmat!', reply_markup=back_m)


@dp.message_handler(Text(equals="🇺🇿 O'zbek"))
async def back(message: types.Message):
    await message.answer('🔝 Asosiy Menyu', reply_markup=menubtn)


@dp.message_handler(Text(equals="👩‍⚕ Bizning xizmatlar"))
async def back(message: types.Message):
    await message.answer('📝 Xizmatni tanlang', reply_markup=xizmat)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
