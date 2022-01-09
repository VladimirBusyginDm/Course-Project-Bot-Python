from re import search, fullmatch, split


class User (object):

    # Имена с заглавной буквы на английском через пробел или тире
    @classmethod
    def validate_user_name(cls, user_name: str) -> bool:
        for word in split(r'[\s-]', user_name):
            if fullmatch(r'\b[A-Z]{1}[a-z]{1,}', word) is None:
                return False
        return True

    # TODO : дописать
    @classmethod
    def validate_country(cls, country: str) -> bool:
        return True

    # число месяц год (разделители : тире)
    @classmethod
    def validate_birthday(cls, age: str) -> bool:
        if fullmatch(r'\b\d{2}[\-]{1,}\d{2}[\-]{1,}\d{4}', age):
            return True
        else:
            return False

    # TODO : дописать
    @classmethod
    def validate_major_language(cls, major_language: str) -> bool:
        return True

    # level : [0,10]
    @classmethod
    def validate_major_language_level(cls, major_language_level: str) -> bool:
        try:
            if (int(major_language_level) >= 0) and (int(major_language_level) <= 10):
                return True
            else:
                return False
        except ValueError:
            return False

    # TODO : дописать
    @classmethod
    def validate_optional_language(cls, optional_language: str) -> bool:
        return True

    # level : [0,10]
    @classmethod
    def validate_optional_language_level(cls, optional_language_level: str) -> bool:
        try:
            if (int(optional_language_level) >= 0) and (int(optional_language_level) <= 10):
                return True
            else:
                return False
        except ValueError:
            return False

    # level : [0, 5]
    @classmethod
    def validate_education(cls, education: str) -> bool:
        try:
            if (int(education) >= 0) and (int(education) <= 5):
                return True
            else:
                return False
        except ValueError:
            return False

    # level : [0, 5]
    @classmethod
    def validate_math_experience(cls, math_experience: str) -> bool:
        try:
            if (int(math_experience) >= 0) and (int(math_experience) <= 5):
                return True
            else:
                return False
        except ValueError:
            return False

    # level : [0, 5]
    @classmethod
    def validate_programming_experience(cls, programming_experience: str) -> bool:
        try:
            if (int(programming_experience) >= 0) and (int(programming_experience) <= 5):
                return True
            else:
                return False
        except ValueError:
            return False

    # level : [0, 70]
    @classmethod
    def validate_work_experience(cls, work_experience: str) -> bool:
        try:
            if (int(work_experience) >= 0) and (int(work_experience) <= 70):
                return True
            else:
                return False
        except ValueError:
            return False
