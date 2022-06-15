"""
GPA Indicator for Honars/Deans list
Lukas Maynard
SDEV - 220
This will show if a student is in honors or on the Deans list based on their GPA
"""

def studentInfo(name, gpa):
    """
    Prints out the name, gpa, and eligibility of Honor roll/Deans list.  
    """
    print('-------------------------------')
    print('Name:', name)
    print('GPA:', gpa)
    if gpa >= 3.5:
        print('Student is on the Deans list.')
    elif 3.25 <= gpa < 3.5:
        print('Student is on the Honor Roll.')
    else:
        print('Student is not on Honor Roll or Deans list.')
    print('-------------------------------\n')

print('\nFind out if a student is in Honors or on the Deans list.\
        \nEnter "ZZZ" as the student name to stop program')

# The main program loop: user can stay or leave when wanted
while True:
    name = str(input('Enter students first and last name: '))
    if name == 'ZZZ':
        print('Thanks for using this GPA indicator.\n')
        break
    gpa = float(input('Enter student GPA: '))
    studentInfo(name, gpa)
    
