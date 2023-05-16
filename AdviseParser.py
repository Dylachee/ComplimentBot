import requests
from bs4 import BeautifulSoup
import json

# Отправить GET-запрос на сайт
url = 'https://www.merriam-webster.com/thesaurus/beautiful'
response = requests.get(url)

# Создать объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Найти div с классом "mw-grid-table-list"
div = soup.find('div', class_='mw-grid-table-list')

# Получить текст из найденного div
content = div.get_text(strip=True)

# Разделить слова на отдельные элементы
words = content.split()

# Создать словарь с данными
data = {
    'content': words
}

# Сохранить данные в файл JSON
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print('Информация успешно сохранена в файле data.json.')
