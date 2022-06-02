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
###########################################################3#


class BlockRu(StatesGroup):
    otdel = State()


class InfoRu(StatesGroup):
    fio = State()


class NumRu(StatesGroup):
    nomer = State()


class UserIdRu(StatesGroup):
    useridru = State()


class FeedbackRu(StatesGroup):
    feedru = State()


#########################################################33


class BlockUz(StatesGroup):
    otdeluz = State()


class InfoUz(StatesGroup):
    fiouz = State()


class NumUz(StatesGroup):
    nomeruz = State()


class UserIdUz(StatesGroup):
    useriduz = State()


class FeedbackUz(StatesGroup):
    feeduz = State()


#######################################################addresult


class AddID(StatesGroup):
    id = State()


class AddRes(StatesGroup):
    result = State()