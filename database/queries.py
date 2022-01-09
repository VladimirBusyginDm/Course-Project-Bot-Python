# DATABASE QUERIES :
INSERT_USER = 'INSERT INTO users_main_information (id, user_name, country, age, major_lang, major_lang_level, optional_lang,' \
              'optional_lang_level, education, math_exp, prog_exp, work_exp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);'

SELECT_USER_BY_ID = 'SELECT * FROM users_main_information WHERE id = ?'

SELECT_ALL = 'SELECT * FROM users_main_information'