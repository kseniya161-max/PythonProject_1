operations = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(operations, state='EXECUTED'):
    """Функция принимает список словарей и возвращает новый список словарей с ключем state по значению"""
    result = []
    for operation in operations:
        if operation.get('state') == state:
            result.append(operation)
    return result


print(filter_by_state(operations, 'EXECUTED'))
print(filter_by_state(operations, 'CANCELED'))



def sort_by_date(operations):
    """Функция принимает список словарей и возвращает список отсортированный по дате"""
    return sorted(operations, key=lambda x: x["date"], reverse=True)


print(sort_by_date(operations))
