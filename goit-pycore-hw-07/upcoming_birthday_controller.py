from datetime import datetime, timedelta
from custom_exceptions import CustomeExceptions

class UpcomingBirthday():
    def determine_congratulation_date(self, birthday: datetime) -> datetime:
        if birthday.weekday() == 5:
            return birthday + timedelta(days=2)
        
        if birthday.weekday() == 6:
            return birthday + timedelta(days=1)
        
        return birthday

    def check_if_birthday_is_within_week(self, today: datetime, birthday: datetime):
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        diff = birthday - today

        if diff.days < 7:
            return True

        return False
    
    def get_upcoming_birthdays(self, usersBirthdays: list[dict]):
        today = datetime.today().date()
        upcoming_birthdays = []
        
        for user in usersBirthdays:
            birthday = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
            birthday = birthday.replace(year=today.year)
            
            if self.check_if_birthday_is_within_week(today, birthday):
                upcoming_birthdays.append({
                  "phone": user["phone"],
                  "name": user["name"],
                  "congratulation_date": self.determine_congratulation_date(birthday),
                })
        
        if not upcoming_birthdays:
            raise CustomeExceptions.BirthdayValidationError("No upcoming birthdays in the address book.")
                
        return upcoming_birthdays