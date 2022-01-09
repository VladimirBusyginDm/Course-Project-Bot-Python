from aiogram import types
from aiogram.dispatcher import FSMContext
from core import dispatcher
from state import States
from keyboard_handler import Keyboard
from chat_models import User
from bot_replicates import EDIT_NAME, EDIT_BIRTHDAY, EDIT_COUNTRY, EDIT_MAJOR_LANGUAGE, EDIT_MAJOR_LANGUAGE_LEVEL,\
    EDIT_OPTIONAL_LANGUAGE, EDIT_OPTIONAL_LANGUAGE_LEVEL, EDIT_EDUCATION, EDIT_MATH_EXPERIENCE, \
    EDIT_PROGRAMMING_EXPERIENCE, EDIT_WORK_EXPERIENCE, EDIT_NOT_VALID_DATA, EDIT_CANCEL, EDIT_END_OF_PROCESS,\
    NO_SUCH_COMMAND


@dispatcher.message_handler(state=States.wait_for_edit_personal_information)
async def wait_for_edit_personal_information(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Yes':
        await message.answer(text=EDIT_NAME, reply_markup=Keyboard.get_cancel_keyboard()),
        await States.wait_for_user_name.set()
    elif message.text == 'No':
        await state.finish()
    else:
        await message.answer(text=NO_SUCH_COMMAND)


@dispatcher.message_handler(state=States.wait_for_user_name)
async def wait_for_user_name(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_user_name(message.text):
        await message.answer(text=EDIT_COUNTRY)
        await States.wait_for_country.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_country)
async def wait_for_country(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_country(message.text):
        await message.answer(text=EDIT_BIRTHDAY)
        await States.wait_for_birthday.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_birthday)
async def wait_for_birthday(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_birthday(message.text):
        await message.answer(text=EDIT_MAJOR_LANGUAGE)
        await States.wait_for_major_lang.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_major_lang)
async def wait_for_major_language(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_major_language(message.text):
        await message.answer(text=EDIT_MAJOR_LANGUAGE_LEVEL)
        await States.wait_for_major_lang_level.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_major_lang_level)
async def wait_for_major_language_level(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_major_language_level(message.text):
        await message.answer(text=EDIT_OPTIONAL_LANGUAGE)
        await States.wait_for_optional_lang.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_optional_lang)
async def wait_for_optional_language(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_optional_language(message.text):
        await message.answer(text=EDIT_OPTIONAL_LANGUAGE_LEVEL)
        await States.wait_for_optional_lang_level.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_optional_lang_level)
async def wait_for_optional_language_level(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_optional_language_level(message.text):
        await message.answer(text=EDIT_EDUCATION)
        await States.wait_for_education.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_education)
async def wait_for_education(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_education(message.text):
        await message.answer(text=EDIT_MATH_EXPERIENCE)
        await States.wait_for_math_experience.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_math_experience)
async def wait_for_math_experience(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_math_experience(message.text):
        await message.answer(text=EDIT_PROGRAMMING_EXPERIENCE)
        await States.wait_for_programming_experience.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_programming_experience)
async def wait_for_programming_experience(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_programming_experience(message.text):
        await message.answer(text=EDIT_WORK_EXPERIENCE)
        await States.wait_for_work_experience.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)


@dispatcher.message_handler(state=States.wait_for_work_experience)
async def wait_for_work_experience(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Cancel':
        await message.answer(text=EDIT_CANCEL, reply_markup=Keyboard.get_start_keyboard())
        await state.finish()
        return
    elif User.validate_work_experience(message.text):
        await message.answer(text=EDIT_END_OF_PROCESS)
        await States.wait_for_major_lang.set()
    else:
        await message.answer(text=EDIT_NOT_VALID_DATA)
    await state.finish()

