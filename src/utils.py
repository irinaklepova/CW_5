from configparser import ConfigParser
import json
import os


def config(filename="data/database.ini", section="postgresql"):
    """ Получение параметров БД """

    # создание парсера
    path_absolute = os.path.abspath(filename)
    parser = ConfigParser()

    # чтение файла конфигурации
    parser.read(path_absolute)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


def load_companies(filename):
    """Получение компаний из файла"""
    result = load_jsonfile(filename)
    return result


def load_jsonfile(filename):
    """Получение данных из json-файла"""
    with open(filename, 'r', encoding='UTF-8') as file:
        result = json.load(file)
    return result
