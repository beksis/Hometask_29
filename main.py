from typing import Dict

def add(a: int, b: int) -> Dict[str, int]:
    result = {'operation': 'addition', 'result': a + b}
    return result

def subtract(a: int, b: int) -> Dict[str, int]:
    result = {'operation': 'subtraction', 'result': a - b}
    return result

def multiply(a: int, b: int) -> Dict[str, int]:
    result = {'operation': 'multiplication', 'result': a * b}
    return result


print(add(8, 10))
print(subtract(15, 3))
print(multiply(21, 4))