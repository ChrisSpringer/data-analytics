# Christopher Springer
# 11/12/2026
# Conditional statements Lab 5: show student and major

student_name = input('Enter student name: ')
student_major = input('Enter major code: ')

print(f'\n{student_name}')
match student_major:
    case 'BIOL':
        print("Biology: Science Bldg, Room 310")
    case 'CSCI':
        print('Computer Science: Sheppard Hall, Room 314')
    case 'ENG':
        print("English: Kerr Hall, Room 201")
    case 'HIST':
        print("History: Kerr Hall, Room 114")
    case 'MKT':
        print("Marketing: Westly Hall, Room 310")
    case _:
        print("<unknown>: No location")