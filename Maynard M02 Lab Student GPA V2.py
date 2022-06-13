"""
GPA Indicator for Honars/Deans list VERSION 2
Lukas Maynard
SDEV - 220
This will show if a student is in honors or on the Deans list based on their GPA
This versiona will let you store data about the students and search for students once they are stored.
"""
students = {}

def addStudent():
    name = str(input('Enter students first and last name: '))
    gpa = float(input('Enter student GPA: '))
    students[name] = gpa
    print('ADDED Student', name)

def studentChoice():
    choice = str(input('Choose student: '))
    if choice not in students.keys():
        print('## Your input was not a student name try again ##')
        studentChoice()
    else:
        studentInfo(choice)

def studentInfo(name):
    print('-------------------------------')
    print('Name:', name)
    print('GPA:', students[name])
    if students[name] >= 3.5:
        print('Student is on Deans list.')
    elif 3.25 <= students[name] < 3.5:
        print('Student is on Honor Roll.')
    else:
        print('Student is not on Honor Roll or Deans list.')
    print('-------------------------------\n')

print('\nFind out if a student is in Honors or on the Deans list.\
        \nPress "a" to add student, "s" for student info, "l" for student list, "ZZZ" to stop program')

while True:
    menuInput = str(input('Enter menu choice: '))
    if menuInput == 'a':
        addStudent()
    elif menuInput == 's':
        studentChoice()
    elif menuInput == 'l':
        print(students.keys())
    elif menuInput == 'ZZZ':
        print('Thanks for using this GPA indicator.\n')
        break
