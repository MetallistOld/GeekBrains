import requests

def currency_rates(val):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.headers['Date']
    response = response.json()
    result = f'{val} = {response["Valute"][val]["Value"]} руб. на {data}'
    return result

if __name__ == '__main__':
    print(currency_rates('EUR'))