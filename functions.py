import datetime

# checks is date in weekend days
def check_weekend(salary_date):
    while salary_date.weekday() in [5, 6]:
        salary_date -= datetime.timedelta(1)
    return salary_date

# dates of closest salary
def get_closest_salary_date(date):

    if date.day > 3:
        answer = "Оклад"
        num, num1 = 17, 3
    else:
        answer = "Аванс"
        num, num1 = 3, 17

    weekdays = [
            "понидельник",
            "вторник",
            "среду",
            "четверг",
            "пятницу"
        ]

    day_of_week = date.weekday()

    salary_date = datetime.date(
        date.year,
        date.month,
        num
    )
    salary_date = check_weekend(salary_date)

    # rewrite date, if its less then corrent
    if salary_date < date:
        salary_date = datetime.date(
            date.year,
            date.month,
            num1
        ) 
        salary_date = check_weekend(salary_date)
        if salary_date < date:
            salary_date = datetime.date(
                date.year,
                date.month+1,
                3
            ) 

    if (date.day in [3, 17] and day_of_week not in [5, 6]) or date == salary_date:
        answer = "Сегодня." 

    elif (salary_date - date).days == 1 and salary_date.weekday() not in [5, 6]:
        answer = "Завтра." 

    elif (salary_date - date).days == 2 and salary_date.weekday() not in [5, 6]:
        answer = f"Послезавтра, в {weekdays[salary_date.weekday()]}." 

    else:        
        answer = answer + f" придёт {salary_date.strftime('%d.%m')}, в {weekdays[salary_date.weekday()]}."
    
    return answer

# dates of prize
def get_prize_date(date):

    month = date.month

    month_str = "этом"

    if date.day > 15:
        month +=1
        month_str = "следующем"

    date_from = datetime.date(
        date.year,
        month,
        10
    )
    while date_from.weekday() in [5,6]:
        date_from += datetime.timedelta(1)

    date_to = datetime.date(
        date.year,
        month,
        15
    )
    while date_to.weekday() in [5,6]:
        date_to -= datetime.timedelta(1)

    answer = f"Премия в {month_str} месяце придет с {date_from.day} по {date_to.day} число."

    return answer