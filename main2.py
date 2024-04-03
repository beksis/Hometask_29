import logging
from typing import Dict

logging.basicConfig(filename='errors.log', level=logging.ERROR,
                    format='%(pastime)s - %(levelname)s - %(message)s')


def add(a: int, b: int) -> Dict[str, int]:
    try:
        result = {'operation': 'addition', 'result': a + b}
        return result
    except Exception as e:
        logging.error(f"Error in addition operation: {e}")


def subtract(a: int, b: int) -> Dict[str, int]:
    try:
        result = {'operation': 'subtraction', 'result': a - b}
        return result
    except Exception as e:
        logging.error(f"Error in subtraction operation: {e}")


def multiply(a: int, b: int) -> Dict[str, int]:
    try:
        result = {'operation': 'multiplication', 'result': a * b}
        return result
    except Exception as e:
        logging.error(f"Error in multiplication operation: {e}")


print(add(8, 'a'))
print(subtract(15, 'b'))
print(multiply('c', 9))
