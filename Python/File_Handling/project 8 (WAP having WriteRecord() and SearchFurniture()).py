from pickle import *

try:
    file = open('Project 8_binary_file.dat', 'x')
    file.close()
except FileExistsError:
    pass


def WriteRecord():
    file = open('Project 8_binary_file.dat', 'ab')
    try:
        FurnitureID = int(input('\nEnter Furniture_ID: '))
        FurnitureName = input('Enter Furniture_Name: ').title()
        Type = input('Enter Furniture_Type: ').title()
        Price = float(input('Enter Furniture_Price: '))
    except ValueError:
        input('invalid input, press enter to go back')
        return
    record = [FurnitureID, FurnitureName, Type, Price]
    dump(record, file)
    file.close()


def SearchFurniture(n):
    file = open('Project 8_binary_file.dat', 'rb')
    print(f'\nrecords of {Type} furniture: ')
    try:
        flag =  1
        while True:
            record = load(file)
            if record[2] == n:
                flag = 0
                print('\nFurniture_ID: ', record[0])
                print('Furniture_Name: ', record[1])
                print('Furniture_Price: ', record[3])
    except EOFError:
        pass
    if flag == 1:
        print('--no records found--')
    file.close()


while True:
    print('\nwhat do you wish to do..?')
    print('1. Add Furniture\n2. search Furniture\n3. exit')
    choice = input('enter choice: ')
    if choice == '1':
        WriteRecord()
    elif choice == '2':
        Type = input('\nenter type of Furniture: ').title()
        SearchFurniture(Type)
    elif choice == '3':
        print('\n--you have exited the program--')
        print('*' * 72)
        break
    else:
        input('invalid choice, press enter to go back')
    print('-' * 72)
