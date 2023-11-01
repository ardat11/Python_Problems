#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    y = s.split(" ")
    liste = []
    for item in y:
        a = item.capitalize()
        liste.append(a)

    res = ""
    for itemm in liste:
        res += itemm

        if liste.index(itemm) != -1:
            res += " "


    return res


if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
