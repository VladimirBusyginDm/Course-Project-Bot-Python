from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    wait_for_edit_personal_information: State = State()
    wait_for_user_name: State = State()
    wait_for_country: State = State()
    wait_for_birthday: State = State()
    wait_for_major_lang: State = State()
    wait_for_major_lang_level: State = State()
    wait_for_optional_lang: State = State()
    wait_for_optional_lang_level: State = State()
    wait_for_education: State = State()
    wait_for_math_experience: State = State()
    wait_for_programming_experience: State = State()
    wait_for_work_experience: State = State()
