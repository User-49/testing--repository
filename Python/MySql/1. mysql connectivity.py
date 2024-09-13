import mysql.connector

sqldb = mysql.connector.connect(user='root', host='localhost', passwd='kapil2006@')
csr = sqldb.cursor()
try:
    database = input('Enter database: ')
    csr.execute(f'use {database}')
except:
    print('\n---database not found---')
    sqldb.close()
    quit()
csr.execute('show tables')
tables = [i[0] for i in csr]
print(tables)
while True:
    print('\nWhat do you wish to do..?')
    print('1. Add tuples')
    print('2. Extract data')
    print('0. exit program')
    choice = input('\nEnter choice: ')
    if choice == '1':
        current_table = input('Enter name of table: ')
        csr.execute(f'describe {current_table}')
        constraints = tuple([i[0] for i in csr])
        if current_table not in tables:
            print('\n---Table not found---')
            continue
        data_type = input('Enter the mode of data insertion(list/manual):').title()
        if data_type == 'List':
            data_list = eval(input('\nEnter nested list:'))
            flag = 0
            for i in data_list:
                if type(i) == list and len(i) == len(constraints):
                    pass
                else:
                    print('\n---incorrect entry---')
                    flag = 1
                    break
            if flag == 0:
                for i in data_list:
                    csr.execute(f'insert into {current_table} values({str(i)[1:-1]})')
                sqldb.commit()
                print('\nDATA ADDED')
                continue
        elif data_type == 'Manual':
            num = int(input('Enter the number of rows to add: '))
            print(f'\ninsert into {current_table} values{constraints}')
            for i in range(1, num + 1):
                csr.execute(f'insert into {current_table} values({input(f'{i}. insert into {current_table} values(')}')
            sqldb.commit()
            print('\nDATA ADDED')
        else:
            print('\n---incorrect entry---')
            continue
    elif choice == '2':
        file = open(f'C:\\Users\\kapil\\OneDrive\\Desktop\\{database}_data.txt', 'w')
        for i in tables:
            file.write(f'{i}:-\n')
            csr.execute(f'describe {i}')
            file.write(str([i[0] for i in csr.fetchall()]) + '\n')
            csr.execute(f'select * from {i}')
            file.writelines([str(i) + '\n' for i in csr.fetchall()])
            file.write('\n')
        print(f'\nData extracted to {database}_data in desktop')
    elif choice == '0':
        print('\n---you have exited the program---')
        print('*' * 72)
        csr.close()
        sqldb.close()
        quit()
    else:
        print('\n---invalid choice---')
    print('\n', '-' * 72)
