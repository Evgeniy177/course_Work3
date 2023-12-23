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
        Создаёт новый EXECUTED список и сортирует его по убыванию
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


def get_requisites(data):
    """
    Форматирование номера счета
    """
    list_of_data = data.split(' ')
    if len(list_of_data[-1]) == 16:
        card_number = list_of_data[-1][0:6] + '*' * 6 + list_of_data[-1][-4:]
        formatted_data = card_number[:4] + ' ' + card_number[4:8] + ' ' + card_number[8:12] + ' ' + card_number[12:]
        list_of_data.pop(-1)
        return ' '.join(list_of_data), formatted_data
    else:
        formatted_data = '**' + list_of_data[-1][-4:]
        list_of_data.pop(-1)
        return ' '.join(list_of_data), formatted_data


def count_payment(transfer):
    """
    Форматирование операции
    """
    payment = transfer['operationAmount']['amount']
    currency = transfer['operationAmount']['currency']['name']
    return payment, currency


def get_description(transfer):
    """
    Вывод описания операции
    """
    return transfer['description']

