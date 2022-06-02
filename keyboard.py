from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

languages = types.InlineKeyboardMarkup(row_width=1)
languages.add(types.InlineKeyboardButton("🇺🇿 O'zbek", callback_data='ozb'))
languages.add(types.InlineKeyboardButton("🇷🇺 Русский", callback_data='ru'))
languages.add(types.InlineKeyboardButton("🇺🇿 Ўзбекча", callback_data='uzb'))
menubtn = types.ReplyKeyboardMarkup(row_width=2)
btn1 = '🧾 Qabul'
btn2 = '✅ Natijalar'
btn3 = '📞 Murojat uchun'
btn4 = '📍 Bizning manzil'
btn5 = '👩‍⚕ Bizning xizmatlar'
btn6 = '📝 Fikr mulohaza'
btn7 = "🇺🇿 Tilni o'zgartirish"
menubtn.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
menubtn_rus = types.ReplyKeyboardMarkup(row_width=2)
btn1 = '🧾 Прием'
btn2 = '✅ Результаты'
btn3 = '📞 Для справки'
btn4 = '📍 Наш адрес'
btn5 = '👩‍⚕ Наши услуги'
btn6 = '📝 Обратная связь'
btn7 = "🇺🇿 / 🇷🇺 Изменить язык"
menubtn_rus.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
back_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_btn = '🔙 Menyuga qaytish'
back_m.add(back_btn)
lang = types.ReplyKeyboardMarkup(row_width=1)
change1 = "🇺🇿 O'zbek"
change2 = "🇷🇺 Русский"
change3 = "🇺🇿 Ўзбекча"
lang.add(change1,change2,change3,back_btn)
xizmat= types.ReplyKeyboardMarkup(row_width=2)
xizmat_btn = ['Терапия','Педиатрия','Гинекология','Урология','Неврапотология','Травматология','Ортопедия','Лаборатория']
xizmat.add(*xizmat_btn, back_btn)


################################################################################################################################################


back_rus = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_ru = '🔙 Вернутся к меню'
back_rus.add(back_ru)
xizmat_ru = types.ReplyKeyboardMarkup(row_width=2)
xizmat_rus = ['Терапия','Педиатрия','Гинекология','Урология','Неврапотология','Травматология','Ортопедия','Лаборатория']
xizmat_ru.add(*xizmat_rus, back_ru)
lang_ru = types.ReplyKeyboardMarkup(row_width=1)
c1 = "🇺🇿 O'zbek"
c2 = "🇷🇺 Русский"
c3 = "🇺🇿 Ўзбекча"
lang_ru.add(c1,c2,c3, back_ru)

########################################################################################

menubtnuz = types.ReplyKeyboardMarkup(row_width=2)
btn1 = '🧾 Кабул'
btn2 = '✅ Натижалар'
btn3 = '📞 Мурожат учун'
btn4 = '📍 Манзилимиз'
btn5 = '👩‍⚕ Бизнинг хизматлар'
btn6 = '📝 Фикр мулоҳаза'
btn7 = "🇺🇿 Тилни ўзгартириш"
menubtnuz.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
back_uzb = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_uz = '🔙 Менюга қайтиш'
back_uzb.add(back_uz)
xizmat_uzb = types.ReplyKeyboardMarkup(row_width=2)
xizmat_uz = ['Терапия','Педиатрия','Гинекология','Урология','Неврапотология','Травматология','Ортопедия','Лаборатория']
xizmat_uzb.add(*xizmat_uz, back_uz)
lang_uzb = types.ReplyKeyboardMarkup(row_width=1)
ch1 = "🇺🇿 O'zbek"
ch2 = "🇷🇺 Русский"
ch3 = "🇺🇿 Ўзбекча"
lang_uzb.add(ch1,ch2,ch3, back_uz)