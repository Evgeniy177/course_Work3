import json
from datetime import datetime
from config import OPERATIONS_PATH

def load_file(file_path):
    """
        Открываем json файл
        :return:
        """
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)
    return data


def sort_list(data, amount=5):
    """
        Создаёт новый EXECUTED список
    """
    new_list = []
    for element in data:
        if not element or element['state'] != 'EXECUTED':
            continue
        new_list.append(element)
        new_list = sorted(new_list, key=lambda operation: operation['date'], reverse=True)
    return new_list[:amount]


def format_date(data):
    """
    Форматирование даты
    """
    date_o = datetime.strptime(data["date"], "%Y-%m-%dT%H:%M:%S.%f")
    return date_o.strftime("%d.%m.%Y")