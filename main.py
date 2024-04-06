import requests


class COLORS:
    WARNING = '\033[93m'
    ENDC = '\033[0m'


def get_area_details() -> tuple:
    area_info = input('Please, enter the area data (Ex. "Sofia, BG"):\n')
    token_city, token_country_code = area_info.split(',')
    c_name = token_city.strip()
    c_code = token_country_code.strip()

    return c_name, c_code


def process_location_request(name: str, code: str, api_key: str) -> dict:
    api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={name},{code}&limit=1&appid={api_key}'

    response = requests.get(api_url)
    data = response.json()[0]
    return data


def process_weather_request(la: float, lo: float, api_key: str):
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={la}&lon={lo}&appid={api_key}&units=metric'

    response = requests.get(api_url)
    data = response.json()
    return data


def display_weather(weather, country):

    icon_id = weather['weather'][0]['icon']
    icon_code = icon_id[0:2]
    message = ""

    if icon_code == '01':
        message = '☀️'
    elif icon_code == '02' or icon_code == '03' or icon_code == '04':
        message = '☁️'
    elif icon_code == '50':
        message = '🌫'
    elif icon_id == '13d':
        message = '❄️'
    elif icon_code == '10' or icon_code == '09':
        message = '🌧'
    elif icon_code == '11':
        message = '🌩'

    print(f'{COLORS.WARNING + " Weather App " + COLORS.ENDC:-^50}')
    print(f'{message: ^40}')
    print(f'\t- City: {weather['name']}, {country}')
    print(f'\t- Weather: {weather['weather'][0]['description']}')
    print(f'\t- Temperature: {weather['main']['temp']: .1f}°C')
    print(f'\t- Feels like: {weather['main']['feels_like']: .1f}°C')
    print(f'\t- Max. temperature: {weather['main']['temp_max']: .1f}°C')
    print(f'\t- Min. temperature: {weather['main']['temp_min']: .1f}°C')
    print(f'\t- Humidity: {weather['main']['humidity']}%')
    print(f'\t- Wind speed: {weather['wind']['speed']} m/s')
    print(f'\t- Cloudiness: {weather['clouds']['all']}%')


key = 'deebc99eaabe2daa3c91fd15635cb964'
city_name, country_code = get_area_details()
location_info = process_location_request(city_name, country_code, key)

lat, lon = location_info['lat'], location_info['lon']
weather_info = process_weather_request(lat, lon, key)
display_weather(weather_info, country_code)
