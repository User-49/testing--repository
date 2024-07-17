from pickle import *

try:
    file = open('Project 6_binary_file.dat', 'x')
    file.close()
except FileExistsError:
    pass


def AddStudent():
    file = open('Project 6_binary_file.dat', 'ab')
    try:
        StudentID = int(input('\nEnter Student_ID: '))
        StudentName = input('Enter Student_Name: ').title()
        Class = int(input('Enter class: '))
        Percentage = float(input('Enter Percentage: '))
    except ValueError:
        input('invalid input, press enter to go back')
        return
    record = [StudentID, StudentName, Class, Percentage]
    dump(record, file)
    file.close()


def SearchStudent(n):
    file = open('Project 6_binary_file.dat', 'rb')
    flag = 1
    print(f'\nRecord of student {n}:')
    try:
        while True:
            record = load(file)
            if record[1] == n:
                print('Student_ID:', record[0])
                print('Student_Name:', record[1])
                print('Class:', record[2])
                print('Percentage:', record[3])
                flag = 0
    except EOFError:
        pass
    if flag == 1:
        print('--record not found--')
    file.close()
    input('\npress enter to go back')


while True:
    print('\nwhat do you wish to do..?')
    print('1. Add student record\n2. Search student record\n3. exit')
    choice = input('enter choice: ')
    if choice == '1':
        AddStudent()
    elif choice == '2':
        StudentName = input('\nEnter the name of student: ').title()
        SearchStudent(StudentName)
    elif choice == '3':
        print('\n--you have exited the program--')
        print('*' * 72)
        break
    else:
        input('invalid input press enter to go back')
    print('-' * 72)
