from aiogram.fsm.state import State, StatesGroup

class ContactForm(StatesGroup):
    name = State()
    phone = State()

class Adverts(StatesGroup):
    adverts = State()