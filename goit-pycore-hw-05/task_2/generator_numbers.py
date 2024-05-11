import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = re.compile(r'\b\d+\.\d+\b') 
    for match in pattern.finditer(text):
        yield float(match.group(0))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    try:
        total = sum(func(text))
        return total
    except TypeError:
        print("Помилка у вхідних даних для сумування.")
        return 0

text = "Загальний дохід працівника складається з декількох частин: 1000.31 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
