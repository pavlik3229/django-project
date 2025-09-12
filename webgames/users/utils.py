from datetime import date



def age_validator(date):
    today = date.today()
    age = today.year - date.year

    if (today.month, today.day) < (date.month, date.day):
        age -= 1
    return age >= 18
