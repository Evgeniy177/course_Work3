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

