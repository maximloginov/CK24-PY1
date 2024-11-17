import json


def task() -> float:
    with open('input.json', 'r') as fd:
        data = json.load(fd)
    total = sum([i['score'] * i['weight'] for i in data])
    return round(total, 3)


print(task())
