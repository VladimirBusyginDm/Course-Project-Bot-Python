from aiogram import types
from core import dispatcher
from state import States
from keyboard_handler import Keyboard
import commands_information as info

@dispatcher.message_handler(commands='start')
async def command_start(message: types.Message) -> None:
    await message.answer(text=info.START_MESSAGE, reply_markup=Keyboard.get_start_keyboard())


@dispatcher.message_handler(commands='inputdata')
@dispatcher.message_handler(lambda message: message.text == 'Input data')
async def command_input_data(message: types.Message) -> None:
    await message.answer(text='Do you wanna edit your personal information ?',
                         reply_markup=Keyboard.get_yes_or_no_keyboard())
    await States.wait_for_edit_personal_information.set()


@dispatcher.message_handler(commands='help')
@dispatcher.message_handler(lambda message: message.text == 'Help')
async def command_help(message: types.Message) -> None:
    await message.answer(text=info.HELP)


@dispatcher.message_handler(commands='author')
@dispatcher.message_handler(lambda message: message.text == 'Author')
async def command_author(message: types.Message) -> None:
    await message.answer(text=info.AUTHOR)


@dispatcher.message_handler(state='*')
async def command_test(message: types.Message) -> None:
    await message.answer(text='This not command...', reply_markup=Keyboard.get_start_keyboard())
