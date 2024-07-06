# Fix the function below so that it becomes pure

students = ['Aparna', 'Anjali', 'Akshay']
teachers = ['Varsha', 'Vivek', 'Vinod']

def all_participants(students, teachers):
    students.extend(teachers)
    return students

everyone = all_participants(students, teachers)
print(everyone)

# Fix the code below so that it becomes pure

from datetime import datetime

def is_month_start():
    today = datetime.now()
    return today.day == 1


def calculate_remaining_credits(credits, spent):
    if is_month_start():
        credits = 500
    return credits - spent

