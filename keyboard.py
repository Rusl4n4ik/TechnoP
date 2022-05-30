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
back_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_btn = '🚫 Bekor qilish'
back_m.add(back_btn)
lang = types.ReplyKeyboardMarkup(row_width=1)
change1 = "🇺🇿 O'zbek"
change2 = "🇷🇺 Русский"
change3 = "🇺🇿 Ўзбекча"
lang.add(change1,change2,change3,back_btn)
xizmat= types.ReplyKeyboardMarkup(row_width=2)
xizmat_btn = ['Терапия','Педиатрия','Гинекология','Урология','Неврапотология','Травматология','Ортопедия','Лаборатория']
xizmat.add(*xizmat_btn, back_btn)