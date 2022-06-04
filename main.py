from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard import languages, menubtn, back_m, lang, xizmat, menubtn_rus, xizmat_ru, back_rus, lang_ru, menubtnuz, xizmat_uzb, lang_uzb, back_uzb
import pathlib
from pathlib import Path
from aiogram.types import ContentType, Message
from fsms import Block, Info, Num, Feedback, UserId, BlockRu, InfoRu, NumRu, UserIdRu, FeedbackRu, BlockUz, InfoUz, NumUz, UserIdUz, FeedbackUz, AddID, AddRes
from db import registration, check_existing, add_user, feedbck, get_result, add_result
from aiogram.dispatcher import FSMContext


API_TOKEN = '5518872025:AAHhkVUhDhsfM7cE6AtX96wRWKSCkMnl6Pw'

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
tmp = {}
tmp1 = {}
tmp2 = {}
tmp3 = {}


# @dp.message_handler(content_types=ContentType.PHOTO)
# async def send_photo_id(message: Message):
#     await message.reply(message.photo[-1].file_id)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=languages)
    exist_user = check_existing(message.chat.id)
    if not exist_user:
        add_user(message.chat.id, message.from_user.first_name, message.from_user.username)


@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    await message.answer('ID:')
    await AddID.id.set()


@dp.message_handler(state=AddID)
async def addid(message: types.Message, state: FSMContext):
    add_id = message.text
    tmp3[message.chat.id] = {}
    tmp3[message.chat.id]['idadd'] = add_id
    await state.finish()
    print(add_id)
    await message.answer('Результат:\nНатижа:')
    await AddRes.result.set()


@dp.message_handler(state=AddRes)
async def addid(message: types.Message, state: FSMContext):
    add_res = message.text
    tmp3[message.chat.id]['resadd'] = add_res
    await state.finish()
    print(add_res)
    add_result(tmp3[message.chat.id]['idadd'], tmp3[message.chat.id]['resadd'])


@dp.callback_query_handler(text='ozb')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Asosiy Menyu:', reply_markup=menubtn)


@dp.message_handler(Text(equals="📞 Murojat uchun"))
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAIBL2KXER1wZmqab0GUc_yNR5SNwa0yAALXvjEbX2qxSH4_jpz-_ps6AQADAgADeAADJAQ',
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
    await message.answer("Namunada ko'rsatilgandek ID kiriting.\nNamuna: 12345 ABCD12", reply_markup=back_m)
    await UserId.userid.set()


@dp.message_handler(state=UserId)
async def userids(message: types.Message, state: FSMContext):
    id = message.text
    print(id)
    try:
        natija = get_result(id)
        print(natija.result)
        await message.answer("Sizning natijaniz: " + natija.result)
        await state.finish()
    except:
        await message.answer('Siz ID noto\'g\'ri kiritdingiz')
        await state.finish()
    # @dp.message_handler(state=UserId)
# async def userids(message: types.Message, state: FSMContext):
#     id = int(message.text.split(" ")[0])
#     print(id)
#     await state.finish()
#     natija = get_result(id)
#     print(natija.result)
#     await message.answer("Sizning natijaniz: " + natija.result)

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
    # await state.finish()
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


@dp.message_handler(Text(equals="🔙 Menyuga qaytish"))
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
    await message.answer('📝 Fikr mulohaza', reply_markup=types.ReplyKeyboardRemove())
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

#############################################################################################RUS


@dp.callback_query_handler(text='ru')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Главное меню: ', reply_markup=menubtn_rus)


@dp.message_handler(Text(equals="🔙 Вернутся к меню"))
async def back(message: types.Message):
    await message.answer('🔝 Главное меню', reply_markup=menubtn_rus)


@dp.message_handler(Text(equals="🧾 Прием"))
async def priem(message: types.Message):
    await message.answer("Выберите раздел, в который хотите записаться",reply_markup=xizmat_ru)
    chat_id = message.from_user.id
    # await bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAOFYpNhhjZJEzeAwZEkRSqc_S4bNbIAAiG9MRsUVKFISiNdp1O4IYcBAAMCAAN5AAMkBA')
    await BlockRu.otdel.set()\



@dp.message_handler(state=BlockRu)
async def priem1(message: types.Message, state: FSMContext):
    block = message.text
    await state.finish()
    print(block)
    await message.answer("Введите свое имя и фамилию:", reply_markup=types.ReplyKeyboardRemove())
    await InfoRu.fio.set()
    tmp[message.chat.id] = {}
    tmp[message.chat.id]['bulim'] = block


@dp.message_handler(state=InfoRu)
async def priem2(message: types.Message, state: FSMContext):
    info = message.text
    await state.finish()
    print(info)
    tmp[message.chat.id]['fio'] = info
    await message.answer("Оставьте свой номер телефона")
    await NumRu.nomer.set()


@dp.message_handler(state=NumRu)
async def priem3(message: types.Message, state: FSMContext):
    text = message.text
    await state.finish()
    print(text)
    tmp[message.chat.id]['text'] = text
    registration(tmp[message.chat.id]['bulim'], tmp[message.chat.id]['fio'], tmp[message.chat.id]['text'])
    await message.answer('Спасибо за информацию', reply_markup=back_rus)


@dp.message_handler(Text(equals="✅ Результаты"))
async def ans(message: types.Message):
    await message.answer("Введите свой ID, как показано в примере.\nПример: 12345 ABCD12", reply_markup=back_rus)
    await UserIdRu.useridru.set()


@dp.message_handler(state=UserIdRu)
async def useridsru(message: types.Message, state: FSMContext):
    id = message.text
    print(id)
    try:
        natija = get_result(id)
        print(natija.result)
        await message.answer("Ваш результат: " + natija.result, reply_markup=back_rus)
        await state.finish()
    except:
        await message.answer('Вы неправильно ввели свой ID', reply_markup=back_rus)
        await state.finish()

@dp.message_handler(Text(equals="🇺🇿 / 🇷🇺 Изменить язык"))
async def back(message: types.Message):
    await message.answer('Выберите язык:', reply_markup=lang_ru)


@dp.message_handler(Text(equals="🇷🇺 Русский"))
async def back(message: types.Message):
    await message.answer('🔝 Главное меню', reply_markup=menubtn_rus)


@dp.message_handler(Text(equals="👩‍⚕ Наши услуги"))
async def back(message: types.Message):
    await message.answer('📝 Выберите услугу', reply_markup=xizmat_ru)


@dp.message_handler(Text(equals="📝 Обратная связь"))
async def back(message: types.Message):
    await message.answer('📝 Обратная связь', reply_markup=types.ReplyKeyboardRemove())
    await FeedbackRu.feedru.set()


@dp.message_handler(state=FeedbackRu)
async def feedback(message: types.Message, state: FSMContext):
    fikr = message.text
    await state.finish()
    tmp1[message.chat.id] = {}
    tmp1[message.chat.id]['feedb'] = fikr
    feedbck(tmp1[message.chat.id]['feedb'])
    print(fikr)
    await message.answer('Спасибо за информацию', reply_markup=back_rus)


@dp.message_handler(Text(equals="📍 Наш адрес"))
async def locationru(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id=chat_id,longitude=66.938027, latitude=39.671019)
    await message.answer("📍 Адрес: Самаркандский район, улица Ходжа Ахрори Вали Манавият 18А\n\nКонтакты:\n☎️ +998 (55) 702-01-02\n☎️ +998 (55) 702-02-03\n👩🏼‍💻 @zuhalmed_admin")


@dp.message_handler(Text(equals="📞 Для справки"))
async def send_photoru(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAIBL2KXER1wZmqab0GUc_yNR5SNwa0yAALXvjEbX2qxSH4_jpz-_ps6AQADAgADeAADJAQ',
                            caption="🏥 Клиника Зухал Мед\n📍 Адрес: Самаркандский район, улица Ходжа Ахрори Вали Манавият 18А\n\nПодать заявку:\n☎️ +998 (55) 702-01-02\n☎️ +998 (55) 702-02-03\n👩🏼‍💻 @zuhalmed_admin"
                            )

#############################################################################################UZB


@dp.callback_query_handler(text='uzb')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Асосий Меню: ', reply_markup=menubtnuz)


@dp.message_handler(Text(equals="🔙 Менюга қайтиш"))
async def back(message: types.Message):
    await message.answer('🔝 Асосий Меню', reply_markup=menubtnuz)


@dp.message_handler(Text(equals="🧾 Кабул"))
async def priemuz(message: types.Message):
    await message.answer("Кабулга ёзилиш учун керакли бўлимни танланг",reply_markup=xizmat_uzb)
    chat_id = message.from_user.id
    # await bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAOFYpNhhjZJEzeAwZEkRSqc_S4bNbIAAiG9MRsUVKFISiNdp1O4IYcBAAMCAAN5AAMkBA')
    await BlockUz.otdeluz.set()\



@dp.message_handler(state=BlockUz)
async def qabuluz(message: types.Message, state: FSMContext):
    block = message.text
    await state.finish()
    print(block)
    await message.answer("Исмингизни ва фамилиянгизни киритинг:", reply_markup=types.ReplyKeyboardRemove())
    await InfoUz.fiouz.set()
    tmp[message.chat.id] = {}
    tmp[message.chat.id]['bulim'] = block


@dp.message_handler(state=InfoUz)
async def qabuluz1(message: types.Message, state: FSMContext):
    info = message.text
    await state.finish()
    print(info)
    tmp[message.chat.id]['fio'] = info
    await message.answer("Малумот учун раҳмат рақамингизни қолдринг")
    await NumUz.nomeruz.set()


@dp.message_handler(state=NumUz)
async def qabuluz2(message: types.Message, state: FSMContext):
    text = message.text
    await state.finish()
    print(text)
    tmp[message.chat.id]['text'] = text
    registration(tmp[message.chat.id]['bulim'], tmp[message.chat.id]['fio'], tmp[message.chat.id]['text'])
    await message.answer('Малумот учун раҳмат', reply_markup=back_uzb)


@dp.message_handler(Text(equals="✅ Натижалар"))
async def ansuz(message: types.Message):
    await message.answer("Намунада кўрсатилган ИД киритинг.\nНамуна: 12345 ABCD12",
                         reply_markup=types.ReplyKeyboardRemove())
    await UserIdUz.useriduz.set()


@dp.message_handler(state=UserIdUz)
async def useridsuz(message: types.Message, state: FSMContext):
    id = message.text
    print(id)
    try:
        natija = get_result(id)
        print(natija.result)
        await message.answer("Сизнинг натижангиз: " + natija.result, reply_markup=back_uzb)
        await state.finish()
    except:
        await message.answer('ИД нотўғри киритдингиз', reply_markup=back_uzb)
        await state.finish()


@dp.message_handler(Text(equals="🇺🇿 Тилни ўзгартириш"))
async def backuz2(message: types.Message):
    await message.answer('Тилни танланг:', reply_markup=lang_uzb)


@dp.message_handler(Text(equals="🇺🇿 Ўзбекча"))
async def backuzz(message: types.Message):
    await message.answer('🔝 Асосий Меню', reply_markup=menubtnuz)


@dp.message_handler(Text(equals="👩‍⚕ Бизнинг хизматлар"))
async def backuzb(message: types.Message):
    await message.answer('📝 Хизматни танланг', reply_markup=xizmat_uzb)


@dp.message_handler(Text(equals="📝 Фикр мулоҳаза"))
async def backuz(message: types.Message):
    await message.answer('📝 Фикр мулоҳаза', reply_markup=types.ReplyKeyboardRemove())
    await FeedbackUz.feeduz.set()


@dp.message_handler(state=FeedbackUz)
async def feedbackuz(message: types.Message, state: FSMContext):
    fikr = message.text
    await state.finish()
    tmp1[message.chat.id] = {}
    tmp1[message.chat.id]['feedb'] = fikr
    feedbck(tmp1[message.chat.id]['feedb'])
    print(fikr)
    await message.answer('Маълумотлар учун рахмат', reply_markup=back_uzb)


@dp.message_handler(Text(equals="📍 Манзилимиз"))
async def locationuz(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id=chat_id,longitude=66.938027, latitude=39.671019)
    await message.answer("📍 Манзил: Самарқанд тумани, Хўжа Ахрори Вали Маинавият кўчаси 18а\n\nКонтактлар:\n☎️ +998 (55) 702-01-02\n☎️ +998 (55) 702-02-03\n👩🏼‍💻 @zuhalmed_admin")


@dp.message_handler(Text(equals="📞 Мурожат учун"))
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAIBL2KXER1wZmqab0GUc_yNR5SNwa0yAALXvjEbX2qxSH4_jpz-_ps6AQADAgADeAADJAQ',
                            caption="🏥 Зуҳал Мед клиникаси \nТаркибидажойлашган манзил: Самарқанд тумани, Хожа Аҳрори Вали Маинавият кўчаси 18А\n\nМурожаат:\n☎️ +998 (55) 702-01-02\n☎️ +998 (55) 702-02-03\n👩🏼‍💻 @zuhalmed_admin")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
