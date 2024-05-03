import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates

# List of countries
countries = ['france', 'germany', 'canada', 'australia', 'united-states', 'united-kingdom', 'switzerland', 'finland']

# Create a CurrencyRates object
cr = CurrencyRates()

# Create a dictionary to map the currency symbols to their respective codes
currency_codes = {
    '€': 'EUR',
    'CA$': 'CAD',
    'A$': 'AUD',
    '$': 'USD',
    '£': 'GBP',
    'CHF': 'CHF'
}

print("hello")


for country in countries: 
    # Send GET request
    res = requests.get(f'https://www.levels.fyi/t/software-engineer/locations/{country}')

    # Parse the result
    soup = BeautifulSoup(res.text, 'html.parser')

    # Find the average salary element
    average_salary_element = soup.find('h3', class_='css-14q3ft1').text

    currency = ''

    salary = average_salary_element.replace(',', '')

    for key in currency_codes.keys():
        if salary.startswith(key):
            currency = currency_codes[key]
            salary = salary.replace(key, '')
            break

    # Convert the salary to USD
    if currency != 'USD' and currency != '':
        salary_in_usd = cr.convert(currency, 'USD', float(salary))
    else:
        salary_in_usd = float(salary)

    # Print the average salary
    print(f'The average software engineer salary in {country.capitalize()} is: ${salary_in_usd:.2f}')

