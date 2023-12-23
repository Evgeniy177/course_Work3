from utils import load_file, sort_list, format_date, get_requisites, count_payment, get_description

file_list = 'operations.json'

data = load_file(file_list)
sorted_list = sort_list(data)

if __name__ == '__main__':
    """
    Выводит данные в нужном формате и последовательности данных по 
    условию задачи
    """
    for transfer in sorted_list:
        date = format_date(transfer)
        description = get_description(transfer)
        payment, currency = count_payment(transfer)
        end_card_name, end_account_number = get_requisites(transfer["to"])
        if len(transfer.keys()) > 6:
            initial_card_name, initial_account_number = get_requisites(transfer["from"])
            print(f'''
                {date} {description}
                {initial_card_name} {initial_account_number} -> {end_card_name} {end_account_number}
                {payment} {currency}
            ''')
        else:
            print(f'''
                {date} {description}
                {end_card_name} {end_account_number}
                {payment} {currency}
            ''')