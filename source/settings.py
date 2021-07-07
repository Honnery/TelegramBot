import configparser

database_config = configparser.ConfigParser()
telegram_config = configparser.ConfigParser()

# ToDo use normal path from os
database_config.read("./configs/database.ini")
telegram_config.read("./configs/telegram.ini")