from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class Keyboard(object):
    __about_project_button: KeyboardButton = KeyboardButton(text='Author')
    __input_data_button: KeyboardButton = KeyboardButton(text='Input data')
    __help_button: KeyboardButton = KeyboardButton(text='Help')
    __model_test_button: KeyboardButton = KeyboardButton(text='Model test')
    __cancel_button: KeyboardButton = KeyboardButton(text='Cancel')
    __yes_button: KeyboardButton = KeyboardButton(text='Yes')
    __no_button: KeyboardButton = KeyboardButton(text='No')
    __step_back_button: KeyboardButton = KeyboardButton(text='Step back')

    @classmethod
    def get_yes_or_no_keyboard(cls):
        return ReplyKeyboardMarkup().add(cls.__yes_button, cls.__no_button)

    @classmethod
    def get_start_keyboard(cls):
        return ReplyKeyboardMarkup().row(cls.__input_data_button, cls.__about_project_button,
                                                             cls.__help_button).add(cls.__model_test_button)

    @classmethod
    def get_cancel_keyboard(cls):
        return ReplyKeyboardMarkup().add(cls.__cancel_button)


