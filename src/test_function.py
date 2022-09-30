import math


def round_down(num, decimal):
    return math.ceil(num * 10 ** decimal) / 10 ** decimal
