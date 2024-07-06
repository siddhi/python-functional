



def add(a, b):
    return a + b



def get_tax(amount, category):
    rate = rates[category]
    if is_cess_applicable(category):
        cess = get_cess_rate(category)
    else:
        cess = 0
    tax = amount * rate/100
    cess = tax * cess/100
    return tax + cess




from datetime import datetime

def is_month_start():
    today = datetime.now()
    return today.day == 1


def calculate_remaining_credits(credits, spent):
    if is_month_start():
        credits = 500
    return credits - spent



students = ['Aparna', 'Anjali', 'Akshay']
teachers = ['Varsha', 'Vivek', 'Vinod']

def all_participants(students, teachers):
    students.extend(teachers)
    return students

everyone = all_participants(students, teachers)
print(everyone)




