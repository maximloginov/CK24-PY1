import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as fd:
        data = [i for i in csv.DictReader(fd)]

    # Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as fd:
        json.dump(data, fd, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
