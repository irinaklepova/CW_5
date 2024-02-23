import requests
import json


class HeadHunter:
    """Класс для получения информации из НН"""
    HH_URL_API = 'https://api.hh.ru/vacancies'

    def get_all_vacancies(self, id):
        """Получение информации о вакансиях"""
        params = {'per_page': 100,
                  'page': 0,
                  'employer_id': id
                  }
        response = requests.get(self.HH_URL_API, params)
        response_data = json.loads(response.text)
        number_pages = response_data['pages']
        result = []

        if 'items' in response_data:
            result.extend(response_data['items'])
        else:
            return result

        if number_pages >= 1:
            for page in range(1, number_pages):
                params['page'] = page
                response = requests.get(self.HH_URL_API, params)
                response_data = json.loads(response.text)
                result.extend(response_data['items'])

        return
