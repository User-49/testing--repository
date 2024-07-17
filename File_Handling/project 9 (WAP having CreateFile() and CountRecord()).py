from pickle import *

try:
    file = open('Project 9_binary_file.dat', 'x')
    file.close()
except FileExistsError:
    pass


def CreateFile():
    file = open('Project 9_binary_file.dat', 'ab')
    try:
        BookNumber = int(input('\nEnter book number: '))
        Book = input('Enter name of book: ').title()
        Author = input('Enter name of author: ').title()
        Price = float(input('Enter price of book: '))
        record = [BookNumber, Book, Author, Price]
        dump(record, file)
    except ValueError:
        input('invalid input, press enter to go back')
    file.close()


def CountRecord(Author):
    if type(Author) != str:
        input('invalid input, press enter to go back')
    file = open('Project 9_binary_file.dat', 'rb')
    books = 0
    print(f'\nnumber of books by {Author}: ', end ='')
    try:
        while True:
            if load(file)[2] == Author:
                books += 1
    except EOFError:
        pass
    if books == 0:
        print(f'--no records of {Author}--')
    print(books)
    file.close()


while True:
    print('\nwhat do you wish to do..?')
    print('1. Add records\n2. Count books by Author\n3. exit')
    choice = input('enter choice: ')
    if choice == '1':
        CreateFile()
    elif choice == '2':
        Author = input('\nEnter name of author: ').title()
        CountRecord(Author)
    elif choice == '3':
        print('\n--you have exited the program--')
        print('*' * 72)
        break
    else:
        input('invalid input, press enter to go back')
    print('-'*72)
