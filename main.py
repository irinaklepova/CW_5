from src.hh_api import HeadHunter
from src.vacancy import Vacancy
from src.DBManager import DBManager
from src.utils import load_companies, config


def main():

    database_name = 'hh_vacancies'
    file_companies_ids = 'data/companies.json'

    # загрузка компаний из файла
    companies = load_companies(file_companies_ids)

    # загрузка параметров БД из database.ini
    params = config()

    # создание БД
    db_manager = DBManager(database_name, params)
    print(f'База SQL {db_manager.name} создана')

    # создание объекта класса HH
    hh_api = HeadHunter()

    for company in companies:
        # получение информации о компании по id
        vacancies_info = hh_api.get_all_vacancies(company['id'])

        # передача информации о компании в БД
        db_manager.insert_data_company(vacancies_info[0])

        # создание списка вакансий
        vacancies = []
        for vacancy_info in vacancies_info:
            vacancy = Vacancy.create_vacancy_from_hh(vacancy_info)
            vacancies.append(vacancy)

        # внесение вакансий в БД
        db_manager.insert_data_vacancy(vacancies)

        print(f"Компания {company['name']} - количество вакансий", len(vacancies_info))
    print('Данные по вакансиям выбранных работодателей добавлены в базу данных SQL')

    # пользовательский интерфейс для работы с БД
    while True:
        print('''
Добрый день!
Выберите один из пунктов
1 - получить список всех компаний и количество вакансий у каждой компании
2 - получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
3 - получить среднюю зарплату по вакансиям
4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
5 - получить список всех вакансий, в названии которых содержится слово python
0 - выход''')

        user_input = input()
        if user_input == "1":
            db_manager.get_companies_and_vacancies_count()
        elif user_input == "2":
            db_manager.get_all_vacancies()
        elif user_input == "3":
            db_manager.get_avg_salary()
        elif user_input == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif user_input == "5":
            db_manager.get_vacancies_with_keyword('python')
        elif user_input == "0":
            break
        else:
            print('Неверная команда')


if __name__ == "__main__":
    main()
