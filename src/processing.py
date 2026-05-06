def filter_by_state(list_dict: list[dict], state="EXECUTED") -> list[dict]:
    """Функция принимает список словарей и отфильтрованный список"""
    filtered_list = []
    for item in list_dict:
        if item["state"] == state:
            filtered_list.append(item)
    return filtered_list


test_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(test_list))


def sort_by_date(my_list_dir: list[dict], descending: bool = True) -> list[dict]:
    """Функция принимает список словарей и задаёт порядок сортировки (по умолчанию — убывание)"""
    sort_by_dates = sorted(my_list_dir, key=lambda x: x["date"], reverse=descending)
    return sort_by_dates


test_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(sort_by_date(test_data))
