from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard import languages, menubtn, back_m, lang, xizmat
import pathlib
from pathlib import Path
from aiogram.types import ContentType, Message
from fsms import Block, Info, Num, Feedback, UserId
from db import registration, check_existing, add_user, feedbck, get_result
from aiogram.dispatcher import FSMContext


API_TOKEN = '5129552109:AAFDehMcyQhuZr-gIvS2QBDNuH4NX0jGpJo'

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
tmp = {}
tmp1 = {}
tmp2 = {}


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=languages)
    exist_user = check_existing(message.chat.id)
    if not exist_user:
        add_user(message.chat.id, message.from_user.first_name, message.from_user.username)


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
    await UserId.userid.set()


@dp.message_handler(state=UserId)
async def userids(message: types.Message, state: FSMContext):
    id = int(message.text.split(" ")[0])
    print(id)
    await state.finish()
    natija = get_result(id)
    print(natija.result)
    await message.answer("Sizning natijaniz: " + natija.result)

# @dp.message_handler(state=UserId)
# async def userids(message: types.Message, state: FSMContext):
#     id = int(message.text.split(" ")[0])
#     tmp2[message.chat.id] = {}
#     tmp2[message.chat.id]['id'] = id
#     print(id)
#     natija = get_result(id)
#     print(natija)
#     await message.answer(natija)
#     await state.finish()
#     await message.answer('Parol kiriting')
#     await Password.pwd.set()

#
# @dp.message_handler(state=Password)
# async def password(message: types.Message, state: FSMContext):
#     pswd = message.text
#     print(pswd)
#     tmp2[message.chat.id]['pwd'] = pswd
#
    await state.finish()
    # natija = get_result(tmp2[message.chat.id]['id'])[0]
    # await message.answer(natija.result)


# @dp.message_handler(Text(equals="✅ Natijalar"))
# async def ans(message: types.Message):
#     await message.answer("Namunada ko'rsatilgandek ID va Parol ni kiriting. ID bo'sh joy Parol\nNamuna: 12345 ABCD12", reply_markup=back_m)
#     await message.answer('ID kiriting:')
#     await UserId.userid.set()
#
#
# @dp.message_handler(state=UserId)
# async def userids(message: types.Message, state: FSMContext):
#     userid = message.text
#     print(userid)
#     # tmp2[message.chat.id] = {}
#     # tmp2[message.chat.id]['id'] = userid
#     await state.finish()
#     natija = get_result(userid)
#     print(natija)
#     await message.answer(natija)

    # await message.answer('Parolni kiriting')
    # await Password.pwd.set()





@dp.message_handler(Text(equals="🚫 Bekor qilish"))
async def back(message: types.Message):
    await message.answer('🔝 Asosiy Menyu', reply_markup=menubtn)


@dp.message_handler(Text(equals="🇺🇿 Tilni o'zgartirish"))
async def back(message: types.Message):
    await message.answer('Tilingizni tanlang:', reply_markup=lang)


@dp.message_handler(Text(equals="🧾 Qabul"))
async def back(message: types.Message):
    await message.answer("Qabulga yozilish uchun kerakli bo'limni tanlang",reply_markup=xizmat)
    chat_id = message.from_user.id
    # await bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAOFYpNhhjZJEzeAwZEkRSqc_S4bNbIAAiG9MRsUVKFISiNdp1O4IYcBAAMCAAN5AAMkBA')
    await Block.bulim.set()


@dp.message_handler(state=Block)
async def bulim(message: types.Message, state: FSMContext):
    block = message.text
    await state.finish()
    print(block)
    await message.answer("Ismingiz va familiyangizni kiriting:", reply_markup=types.ReplyKeyboardRemove())
    await Info.ism_fam.set()
    tmp[message.chat.id] = {}
    tmp[message.chat.id]['bulim'] = block


@dp.message_handler(state=Info)
async def bulim(message: types.Message, state: FSMContext):
    info = message.text
    await state.finish()
    print(info)
    tmp[message.chat.id]['fio'] = info
    await message.answer("Telefon raqamingizni qoldring")
    await Num.telefon.set()


@dp.message_handler(state=Num)
async def bulim(message: types.Message, state: FSMContext):
    text = message.text
    await state.finish()
    print(text)
    tmp[message.chat.id]['text'] = text
    registration(tmp[message.chat.id]['bulim'], tmp[message.chat.id]['fio'], tmp[message.chat.id]['text'])
    await message.answer('Malumot uchun rahmat', reply_markup=back_m)


@dp.message_handler(Text(equals="📝 Fikr mulohaza"))
async def back(message: types.Message):
    await message.answer('📝 Fikr mulohaza')
    await Feedback.ftxt.set()


@dp.message_handler(state=Feedback)
async def feedback(message: types.Message, state: FSMContext):
    fikr = message.text
    await state.finish()
    tmp1[message.chat.id] = {}
    tmp1[message.chat.id]['feedb'] = fikr
    feedbck(tmp1[message.chat.id]['feedb'])
    print(fikr)
    await message.answer('Fikr-mulohaza uchun rahmat!', reply_markup=back_m)


@dp.message_handler(Text(equals="🇺🇿 O'zbek"))
async def back(message: types.Message):
    await message.answer('🔝 Asosiy Menyu', reply_markup=menubtn)


@dp.message_handler(Text(equals="👩‍⚕ Bizning xizmatlar"))
async def back(message: types.Message):
    await message.answer('📝 Xizmatni tanlang', reply_markup=xizmat)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
