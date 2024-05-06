import requests
import json
from bs4 import BeautifulSoup
from fake_headers import Headers


def json_write(data):
    with open('search_result.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        print(json_str)


keywords = ['Django', 'Flask']
cities = ['Москва', 'Санкт-Петербург']
data_list = []

headers_generator = Headers(os='win', browser='chrome')

response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2',
                        headers=headers_generator.generate())

main_html_data = response.text
main_soup = BeautifulSoup(main_html_data, 'lxml')
vacancies_list = main_soup.find('div', id='a11y-main-content')
vacancies = vacancies_list.find_all('div', class_='vacancy-serp-item__layout')

for vacancy in vacancies:
    title_tag = vacancy.find('span', class_='serp-item__title-link serp-item__title')
    title = title_tag.text

    vacancy_link_tag = vacancy.find('a', class_='bloko-link')
    link = vacancy_link_tag['href']

    city_tag = vacancy.find('div', class_='vacancy-serp-item-body__main-info').text
    for town in cities:
        if town in city_tag:
            city = town
        else:
            pass

    response = requests.get(url=link, headers=headers_generator.generate())
    vacancy_data = response.text

    vacancy_soup = BeautifulSoup(vacancy_data, 'lxml')

    description_tag = vacancy_soup.find('div', class_='g-user-content')
    description = description_tag.text

    salary_tag = vacancy_soup.find('span', class_='bloko-header-section-2')
    salary = salary_tag.text

    if '$' in salary or '₽' in salary or '€' in salary:
        salary = salary.split()
        salary = ' '.join(salary)
    else:
        salary = 'ЗП не указана'

    employee_tag = vacancy_soup.find('span', class_='vacancy-company-name')
    employee = employee_tag.text

    for keyword in keywords:
        if keyword in description and ('$' in salary or '₽' in salary or '€' in salary):
            data = {
                'link': link,
                'salary': salary,
                'employee': employee,
                'city': city
            }
            if data in data_list:
                continue
            data_list.append(data)

json_write(data_list)