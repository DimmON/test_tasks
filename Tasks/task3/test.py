from Tasks.task1.test import print_technic
from Tasks.task2.test import add_files


def start_tasks():
    print_technic()

    print()

    files = [
        'aaaaaaaaa.txt',
        'abc.boc',
        'qwerty.xls'
    ]
    print(add_files(files))
