from aiogram.dispatcher.filters.state import StatesGroup, State


class Block(StatesGroup):
    bulim = State()


class Info(StatesGroup):
    ism_fam = State()


class Num(StatesGroup):
    telefon = State()


class Feedback(StatesGroup):
    ftxt = State()


class UserId(StatesGroup):
    userid = State()
#
#
# class Password(StatesGroup):
#     pwd= State()