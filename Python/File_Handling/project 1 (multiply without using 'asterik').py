def multiply(num_a, num_b):
    multiple = int()
    for i in range(abs(num_a)):
        multiple += abs(num_b)
    if (num_a < 0) != (num_b < 0):
        multiple = - multiple
    return multiple


a = int(input('enter first number: '))
b = int(input('enter second number: '))
print('multiple of first and second number is,', multiply(a, b))
temp = input('press any key to exit')
exit()
