queue = list()
while True:
    print('what do you wish to do..')
    print('1. Insert Element\n2. Delete Element\n3. Display Queue\n4. Peek Element\n5. Exit')
    choice = input('Enter choice: ')
    if choice == '1':
        element = input('\nEnter element: ')
        queue.append(element)
    elif choice == '2':
        if not queue:
            print('\nUnderflow')
        else:
            print('\nDeleted element is', queue.pop(0))
    elif choice == '3':
        print('\nQueue:')
        if not queue:
            print('queue empty')
        else:
            for i in queue:
                print(i)
    elif choice == '4':
        if not queue:
            print('\nqueue empty')
        else:
            print('\nElement at front: ', queue[0])
    elif choice == '5':
        print('\n--you have exited the program--')
        print('*' * 72)
        break
    else:
        input('invalid input, press enter to go back')
    print('\n', '-' * 72)
