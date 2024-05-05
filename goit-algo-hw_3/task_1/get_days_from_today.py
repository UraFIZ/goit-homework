from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.now()
        diff = current_date - input_date
        return diff.days
    except ValueError as e:
        print(f"Виникла помилка з датою: {e}")
        return None  # Повертаємо None, якщо дата невірна

# Приклад використання
result = get_days_from_today('2024-04-30')
if result is not None:
    print(f"Кількість днів від вказаної дати: {result}")
else:
    print("Будь ласка, перевірте формат введеної дати, наприклад, 2024-12-31.")
