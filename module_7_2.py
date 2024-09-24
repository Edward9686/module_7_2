def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            start_byte = file.tell()  # Получаем номер байта перед записью
            file.write(string + '\n')  # Записываем строку в файл
            strings_positions[(i, start_byte)] = string  # Сохраняем информацию в словарь

    return strings_positions


# Пример использования функции
file_name = 'output.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
result = custom_write(file_name, strings)

print(result)

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
