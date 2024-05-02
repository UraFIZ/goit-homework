import re

def normalize_phone(phone_number):
    prepared_number = re.sub(r'[^\d+]', '', phone_number.strip())

    match prepared_number:
        case number if number.startswith('+'):
            return number
        case number if number.startswith('380'):
            return '+' + number
        case _:
            return '+38' + prepared_number
    