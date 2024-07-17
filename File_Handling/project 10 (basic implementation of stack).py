stack = list()
while True:
    print('what do you wish to do..?')
    print('1. Push element\n2. Pop element\n3. Display stack\n4. exit program')
    choice = input('Enter choice: ')
    if choice == '1':
        element = input('\nEnter element to push: ')
        stack.append(element)
    elif choice == '2':
        if not stack:
            print('\nunderflow')
        else:
            print(f'\nDeleted element is: {stack.pop()}')
    elif choice == '3':
        print('\nStack:')
        length = len(stack)
        if not stack:
            print('--Stack empty--')
        else:
            for i in range(length - 1, -1, -1):
                if i == length - 1:
                    print(f'{stack[i]} <--TOP')
                else:
                    print(stack[i])
    elif choice == '4':
        print('\n--you have exited the program--')
        print('*'*72)
        break
    else:
        input('invalid input, press enter to go back')
    print('\n', '-'*72)
