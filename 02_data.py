students = ['Aparna', 'Anjali', 'Akshay']
teachers = ['Varsha', 'Vivek', 'Vinod']

def all_participants(students, teachers):
    return students + teachers

everyone = all_participants(students, teachers)
print(everyone)




def get_student_fn(students, index):
    def get():
        return students[index]
    return get

students = ['Aparna', 'Anjali', 'Akshay']
fn = get_student_fn(students, 1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = Point(2, 5)
b = Point(2, 5)
a.x = 10

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

a = Point(2, 5)
b = Point(2, 5)
print(a == b)



