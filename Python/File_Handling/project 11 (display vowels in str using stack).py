string = input('Enter string: ')
stack = []
for i in string:
    if i in 'aeiouAEIOU':
        if i not in stack:
            stack.append(i)
print('\nstack:')
if not stack:
    print('Stack Empty')
else:
    for i in range(len(stack)-1, -1, -1):
        if i == len(stack)-1:
            print(f'{stack[i]}<--TOP')
        else:
            print(stack[i])
print(f'The number of unique vowels in the given string: {len(stack)}')
