number = int(input('Enter number: '))
reversed_number = int()

# 1234

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f'Reversed number = {reversed_number}')