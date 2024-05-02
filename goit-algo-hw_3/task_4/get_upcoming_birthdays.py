from datetime import datetime, timedelta

def determine_congratulation_date(birthday: datetime) -> datetime:
    if birthday.weekday() == 5:
        return birthday + timedelta(days=2)
    
    if birthday.weekday() == 6:
        return birthday + timedelta(days=1)
    
    return birthday

def check_if_birthday_is_within_week(today: datetime, birthday: datetime):
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
    diff = birthday - today
    
    if diff.days < 7:
        return True
    
    return False

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday = birthday.replace(year=today.year)
        
        if check_if_birthday_is_within_week(today, birthday):
            upcoming_birthdays.append({
              "name": user["name"],
              "congratulation_date": determine_congratulation_date(birthday),
            })
            
    return upcoming_birthdays



users = [
    {"name": "John Doe", "birthday": "1985.05.02"},
    {"name": "Jane Smith", "birthday": "1990.04.25"}
]

print(get_upcoming_birthdays(users))