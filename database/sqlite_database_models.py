from peewee import *
from sqlite_database_configuration import DATABASE_USERS_PATH, DATABASE_USERS_INFORMATION_NAME


class BaseModel(Model):
    class Meta:
        database: SqliteDatabase = SqliteDatabase(database=DATABASE_USERS_PATH)


class UserInformationModel(BaseModel):
    id: PrimaryKeyField = PrimaryKeyField(unique=True)
    name: CharField = CharField()
    country: CharField = CharField()
    birthday: IntegerField = IntegerField()
    major_language: CharField = CharField()
    major_language_level: IntegerField = IntegerField()
    optional_language: CharField = CharField()
    optional_language_level: IntegerField = IntegerField()
    education: IntegerField = IntegerField()
    math_experience: IntegerField = IntegerField()
    programming_experience: IntegerField = IntegerField()
    work_experience: IntegerField = IntegerField()