from typing import List


def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
    return len(list(filter(lambda x: x >= target, hours)))


hours = [10, 20, 30, 40, 50]
target = 30
print(numberOfEmployeesWhoMetTarget(hours, target))
