number = int(input('Enter number: '))
test_number, temp_number = int(), number
while temp_number != 0:
    test_number += (temp_number % 10)**3
    temp_number //= 10
if test_number == number:
    print(f"The number {number} is an angstrom's number")
else:
    print(f"The number {number} is not an angstrom's number")
