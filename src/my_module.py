import numpy as np
import logging


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("MIANOWNIK NIE MOŻE MIEĆ ZERA")
    return a / b


def calculate_mean(numbers):
    logging.info("Calculating mean")
    return np.mean(numbers)