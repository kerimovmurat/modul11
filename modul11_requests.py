import requests

# Ваш API-ключ
api_key = '33627dbddd23c18ae50aadd5b54ab4b8'  # Замените на ваш реальный ключ
city = 'Moscow'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    data = response.json()  # Получаем данные в формате JSON
    print(f"Погода в {city}:")
    print(f"Температура: {data['main']['temp']}°C")
    print(f"Описание: {data['weather'][0]['description']}")
else:
    print(f'Ошибка: {response.status_code}, сообщение: {response.text}')
