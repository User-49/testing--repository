from pickle import load, dump

try:
    file = open('Project 15_binary_file.dat', 'x')
    file.close()
except FileExistsError:
    pass


def open_file(mode):
    return open('Project 15_binary_file.dat', mode)


def records():
    try:
        file = open_file('rb')
        l = list()
        while True:
            l.append(load(file))
    except EOFError:
        file.close()
        return l


while True:
    print('What do you wish to do..?')
    print('1. Insert record\n2. Display record\n3. Update record\n4. Search record\n5. Delete record\n6. Exit')
    choice = input('Enter choice: ')
    if choice == '1':
        file = open_file('ab')
        name = input('\nEnter name of student: ').title()
        roll_num = int(input('Enter roll number of student: '))
        marks = float(input('Enter marks: '))
        record = {'Name': name, 'Roll Number': roll_num, 'Marks': marks}
        dump(record, file)
        file.close()
    elif choice == '2':
        print('\nRecords:')
        for i in records():
            print(i)
        if not records():
            print('--records not found--')
    elif choice == '3':
        roll_num = int(input('\nEnter roll number of student: '))
        flag = 1
        record = records()
        for i in record:
            if i['Roll Number'] == roll_num:
                i['Marks'] = int(input('Enter new marks: '))
                file = open_file('wb')
                for i in record:
                    dump(i, file)
                print('--Record added--')
                file.close()
                flag = 0
                break
        if flag == 1:
            print('--no records found--')
    elif choice == '4':
        roll_num = int(input('\nEnter roll number of student: '))
        flag = 1
        for i in records():
            if i['Roll Number'] == roll_num:
                print('\nStudent record:')
                print('Student Name: ', i['Name'])
                print('Marks: ', i['Marks'])
                flag = 0
                break
        if flag == 1:
            print('--no records present--')
    elif choice == '5':
        roll_num = int(input('\nEnter roll number of student: '))
        flag = 1
        record = records()
        for i in record:
            if i['Roll Number'] == roll_num:
                record.remove(i)
                file = open_file('wb')
                for i in record:
                    dump(i, file)
                print('--Record deleted--')
                flag = 0
                file.close()
                break
        if flag == 1:
            print('--no records found--')
    elif choice == '6':
        print('\n--you have exited the program--')
        print('*' * 72)
        break
    else:
        input('invalid input, press enter to go back')
    print('\n', '-' * 72)
