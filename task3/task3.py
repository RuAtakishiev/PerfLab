import os
import json
from typing import Any

value_file_path = input("Введите путь для файла \"values.json\": ")
tests_file_path = input("Введите путь для файла \"tests.json\": ")
report_file_path = input("Введите путь для файла \"report.json\": ")
flag = False

if os.path.exists(value_file_path) and os.path.exists(tests_file_path):
    with open(value_file_path, mode='r', encoding='utf8') as value_file:
        value_data_json = json.load(value_file)
    
    with open(tests_file_path, mode='r', encoding='utf8') as tests_file:
        test_data_json = json.load(tests_file)
    
else:
    raise FileNotFoundError('Файлы не найдены')


dict_id_value = {item['id']: item['value'] for item in value_data_json['values']} 

def recursion_func(data: Any) -> None:
    if isinstance(data, dict):
        if 'id' in data and data['id'] in dict_id_value:
            data['value'] = dict_id_value[data['id']]

        for item in data.values():
            recursion_func(item)

    elif isinstance(data, list):
        for item in data:
            recursion_func(item)

recursion_func(test_data_json)

with open(report_file_path, mode='w', encoding='utf8') as file_write:
    json.dump(test_data_json, file_write, indent=4)
