import json

# Загрузить данные из файла JSON
with open('compliments.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Получить список комплиментов
compliments = data['compliments']

# Разделить комплименты на списки по символу '\n'
compliment_lists = '\n'.join(compliments).split('\n')

# Удалить пустые строки из списков
compliment_lists = list(filter(None, compliment_lists))

# Сохранить разделенные комплименты в файл JSON
data_with_separator = {'compliments': compliment_lists}

with open('compliments.json', 'w', encoding='utf-8') as file:
    json.dump(data_with_separator, file, ensure_ascii=False, indent=4)

print("Комплименты успешно разделены и сохранены в файле compliments.json")
