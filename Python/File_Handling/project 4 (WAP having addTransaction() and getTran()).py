from csv import *


def openFile(mode):
    try:
        file = open('Project 4_csv_file.csv', 'x')
        file.close()
    except FileExistsError:
        file = open('Project 4_csv_file.csv', mode, newline='')
    else:
        file = open('Project 4_csv_file.csv', 'a', newline='')
        writer(file).writerow(['TranID', 'TranDate', 'Amount', 'Type'])
        file.close()
        file = open('Project 4_csv_file.csv', mode, newline='')
    return file


def addTransaction():
    file = openFile('a')
    csw = writer(file)
    try:
        TranID = int(input('\nEnter transaction id: '))
        TranDate = input('Enter date of transaction(dd-mm-yyyy): ')
        Amount = int(input('Enter amount of transaction: '))
        Type = input('Enter type of transaction: ').title()
    except ValueError:
        input('invalid input,press enter to go back')
        return
    input_list = [TranID, TranDate, Amount, Type]
    csw.writerow(input_list)
    file.close()


def getTran():
    file = openFile('r')
    csr = reader(file, delimiter=',')
    print('\nDeposit Records:')
    flag = 1
    for i in csr:
        if csr.line_num != 1:
            if i[3] == 'Deposit':
                print(i, csr.line_num)
                flag = 0
    if flag == 1:
        print('--No deposit records found--')
    file.close()


while True:
    print('what do wish to do...?')
    print('1. Add a transaction\n2. Display deposit transaction\n3. exit')
    try:
        choice = int(input('Enter choice: '))
        assert choice in range(1, 4)
    except ValueError or AssertionError:
        input('invalid input, press enter to go back')
    else:
        if choice == 1:
            addTransaction()
        elif choice == 2:
            getTran()
        else:
            break
        print('-' * 72, '\n')
33
