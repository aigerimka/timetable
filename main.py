from timetable import *
import json


def main():
    our_subjects = []
    with open('schedule.txt', encoding='utf-8') as f:
        for line in f.readlines():
            day = Subjects(json.loads(line))
            our_subjects.append(str(day).split(', '))
    print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format('1 пара', '2 пара', '3 пара', '4 пара'))
    print('-' * 65)
    for i in our_subjects:
        table = Timetable(i)
        print(table)


if __name__ == '__main__':
    main()
