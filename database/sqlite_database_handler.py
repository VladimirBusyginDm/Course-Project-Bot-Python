from sqlite_database_models import UserInformationModel
from peewee import *


class SQLiteDatabase(object):
    __user_information_db: SqliteDatabase = UserInformationModel.database

    @classmethod
    def write_user_information(cls, information: tuple) -> bool:
        UserInformationModel.insert()

