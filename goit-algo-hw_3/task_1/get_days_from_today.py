from datetime import datetime


def get_days_from_today(date: str) -> int:
    input_date = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.now()
    diff = current_date - input_date
    
    return diff.days

print(get_days_from_today('2024-04-30'))


