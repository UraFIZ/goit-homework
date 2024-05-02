from decorators import log_errors

def calculate_total_and_average_salary(salaries: list) -> tuple[int, int]:
  total_salary = sum(map(int, salaries))
  return total_salary, total_salary // len(salaries)


def fetch_data(path: str) -> list:
  try:
    with open(path, 'r', encoding='utf-8') as file:
      data = [line.strip() for line in file.readlines()]
      if not data:
        raise ValueError(f"{fetch_data.__name__}: Файл порожній. Будь ласка, перевірте контент файлу.")
      return data
  except FileNotFoundError:
    raise FileNotFoundError(f"{fetch_data.__name__}: Файл не знайдено. Перевірте шлях до файлу.")


def extract_salary_amount(data: list) -> list:
  salaries = []
  for item in data:
    parts = item.split(',')
    if len(parts) != 2:
      raise ValueError(f"{extract_salary_amount.__name__}: Некоректний формат даних у рядку: {item}, очікується ім'я і зарплата")

    _, salary = parts
    if not salary.isdigit():
      raise ValueError(f"{extract_salary_amount.__name__}: Зарплата містить недопустимі символи: {salary} (у рядку: {item})")

    salaries.append(salary)
  return salaries


def calculate_salary(path: str) -> tuple[int, int] | tuple[None, None]:
  try:
    salaries_data = fetch_data(path)
    salaries_list = extract_salary_amount(salaries_data)
    return calculate_total_and_average_salary(salaries_list)
  except Exception as e:
    print(f'{calculate_salary.__name__}: Маємо наступну помилку -> {e}')
    # Повертаємо None, None, щоб не трігерити помилку далі в chain
    return None, None



@log_errors
def prepare_salary_report(path: str) -> None:
  total, average = calculate_salary(path)
  if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
  else:
    print("Не вдалося обрахувати зарплату.")


prepare_salary_report('employees_salary.txt')