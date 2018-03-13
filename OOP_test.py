class Student:

    def __init__(elf, first, last, course):
        elf.first = first
        elf.last = last
        elf.course = course
        elf.email = first + last+ '@nasa_jpl.us'

    def fullname(elf):
        return '{} {}'.format(elf.first, elf.last)

stdnt1 = Student('Neil', 'Armstrong', 'Physics')
stdnt2 = Student('Michael', 'Collins', 'Engineering')
stdnt3 = Student('Buzz', 'Aldrin', 'Aeronautics')

print(stdnt1.fullname())
print(stdnt2.fullname())
print(stdnt3.fullname())
