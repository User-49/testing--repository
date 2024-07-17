from csv import *

try:
    file = open('Project 5_csv_file.csv', 'x')
    file.close()
except FileExistsError:
    pass
else:
    file = open('Project 5_csv_file.csv', 'a')
    writer(file).writerow(['ProductID', 'ProductName', 'Price'])
    file.close()


def AddRecord():
    file = open('Project 5_csv_file.csv', 'a')
    ProductID = int(input('\nEnter product_ID: '))
    ProductName = input('Enter Product_Name: ')
    Price = float(input('Enter Product_Price: '))
    record = [ProductID, ProductName, Price]
    writer(file).writerow(record)
    file.close()


def DisplayRecord(n):
    file = open('Project 5_csv_file.csv', 'r', newline='\n')
    csr = reader(file)
    print(f'\nRecords of Price > {n}:')
    flag = 1
    for i in csr:
        if csr.line_num != 1:
            if float(i[2]) > n:
                print(i)
                flag = 0
    if flag == 1:
        print('--no records found--')
    file.close()


while True:
    print('\nwhat do you wish to do..?')
    print('1.Add Record\n2. Display records\n3. Exit:')
    choice = input('enter choice: ')
    if choice == '1':
        AddRecord()
    elif choice == '2':
        price = float(input('\nEnter Price: '))
        DisplayRecord(price)
    elif choice == '3':
        print('\n--you have exited the program--')
        print('*' * 72)
        break
    else:
        input('invalid input,press enter to go back')
    print('-' * 72)
