# import json
import math
import random


def calculate_sin(number):
    return math.sin(math.radians(number))


def calculate_cos(number):
    return math.cos(math.radians(number))


def generate_random_number(start, end):
    return random.randint(start, end)
