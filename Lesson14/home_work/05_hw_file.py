import json
import os
from unittest import result


def calculate_salary(workers, hours):
    workers_dict = {}
    result = {}

    with open(workers, 'r', encoding='utf-8') as f:
        for line in f:
            name, salary, norm_hours = line.split()
            salary = int(salary)
            norm_hours = int(norm_hours)

        workers_dict[name] = {'salary': salary, 'norm_hours': norm_hours}

    with open(hours, 'r', encoding='utf-8') as f:
        for line in f:
            name, hours = line.split()
            result[name] = workers_dict[name]['salary'] * int(hours) / int(workers_dict[name]['norm_hours'])
        return result


calculate_salary(
    workers='data/workers.txt',
    hours='data/hours.txt')
