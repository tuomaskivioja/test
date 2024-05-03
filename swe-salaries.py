import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates

c = CurrencyRates()

countries = ['france', 'germany', 'canada', 'australia', 'united-states', 'united-kingdom', 'switzerland', 'finland']

currency_codes = {
    '€': 'EUR',
    'CA$': 'CAD',
    'A$': 'AUD',
    '$': 'USD',
    '£': 'GBP',
    'CHF': 'CHF'
}


for country in countries:
    res = requests.get(f'https://www.levels.fyi/t/software-engineer/locations/{country}')

    soup = BeautifulSoup(res.text, 'html.parser')

    average_salary_element = soup.find('h3', {'class': 'css-143ft1'}).text

    salary = average_salary_element.replace(',', '')

    currency = ''

    for key in currency_codes.keys():
        if salary.startswith(key):
            currency = currency_codes[key]
            salary = salary.replace(key, '')
            break
    

    if currency != 'USD' and currency != '':
        salary_in_usd = c.convert(currency, 'USD', float(salary))
    else:
        salary_in_usd = float(salary)

    print(f'The average software engineer salary in {country.capitalize()} is: ${salary_in_usd:.2f}')


