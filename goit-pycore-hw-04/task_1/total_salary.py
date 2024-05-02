def calculate_total_and_average_salary(salaries: list) -> tuple[int, int]:
  total_salary = sum(map(int, salaries))
  return total_salary, total_salary // len(salaries)


def fetch_data(path: str) -> list:
  try:
    with open(path, 'r', encoding='utf-8') as file:
      data = [line.strip() for line in file.readlines()]
      if not data:
        raise ValueError("fetch_data: Файл порожній. Будь ласка, перевірте контент файлу.")
      return data
  except FileNotFoundError:
    raise FileNotFoundError('fetch_data: Файл не знайдено')


def extract_salary_amount(data: list) -> list:
  salaries = []
  for item in data:
    parts = item.split(',')
    if len(parts) != 2:
      raise ValueError(f"extract_salary_amount: Некоректний формат даних у рядку: {item}, очікується ім'я і зарплата")

    _, salary = parts
    if not salary.isdigit():
      raise ValueError(f"extract_salary_amount: Зарплата містить недопустимі символи: {salary} (у рядку: {item})")

    salaries.append(salary)
  return salaries


def calculate_salary(path: str) -> tuple[int, int] | tuple[None, None]:
  try:
    salaries_data = fetch_data(path)
    salaries_list = extract_salary_amount(salaries_data)
    return calculate_total_and_average_salary(salaries_list)
  except Exception as e:
    print(f'calculate_salary: Маємо наступну помилку -> {e}')
    # Повертаємо None, None, щоб не трігерити помилку в глобальному контексті використання функції
    return None, None


try:
  total, average = calculate_salary('employees_salary.tx')
  if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
  else:
    print("Не вдалося обрахувати зарплату.")
except Exception as e:
  # Помилка буде виникати тільки (можливо) в разі, якщо відсутній аргумент у функції calculate_salary
  print(f'Основна помилка: {e}')