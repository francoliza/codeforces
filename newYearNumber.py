#!/home/franco/anaconda3/bin/python3

import math
import os
import random
import re
import sys


def isDivisibleBy2020Or2021(num):
    if num == 0:
        return True
    elif num < 2020:
        return False
    return (isDivisibleBy2020Or2021(num - 2020) or isDivisibleBy2020Or2021(num - 2021))


def newYearNumber(arr):
    for num in arr:
        if (isDivisibleBy2020Or2021(num)):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    n = int(input())

    arr = list()
    for i in range(0, n):
        num = int(input())
        arr.append(num)

    newYearNumber(arr)