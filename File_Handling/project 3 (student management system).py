student_records = dict()


def choices(x):
    try:
        ch = int(input('enter choice: '))
        if ch in range(1, 1 + x):
            return ch
        raise Exception
    except Exception or ValueError:
        input('invalid input, press enter to go back')


while True:
    print('what do you wish to do..?')
    print('1. Add Students')
    print('2. Update Marks')
    print('3. Remove Students')
    print('4. Marks Report')
    choice = choices(6)
    if choice == 1:
        name = input('\nEnter name of the student: ')
        if name in student_records:
            print('--record already exists--')
        else:
            student_records[name] = int()
    elif choice == 2:
        name = input('\nEnter name of student: ')
        if name in student_records:
            marks = float(input('Enter marks of student: '))
            student_records[name] = marks
        else:
            print("--Records don't exist--")
    elif choice == 3:
        name = input('\nEnter name of student: ')
        if name in student_records:
            if 'CONFIRM' == input('Enter "CONFIRM" to permanently delete the record: '):
                del student_records[name]
        else:
            print("--Records don't exist--")
    elif choice == 4:
        print('\n', '-' * 72, '\nHow do you wish to print records..?')
        print('1. Ascending\n2. Descending')
        choice = choices(2)
        if choice == 1:
            ordered_list = list(student_records.items())
            ordered_list = ordered_list.sort(key=lambda x: x[1])
            print('\nname\t\tmarks')
            for i in ordered_list:
                print(i[0], i[1])
        elif choice == 2:
            ordered_list = list(student_records.items()).sort(key=lambda x: x[1], reverse=True)
            print('\nname\t\tmarks')
            for i in ordered_list:
                print(i[0], i[1])
    print('\n', '-' * 72)
