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
print(fn())
students[1] = 'Anand'
print(fn())



