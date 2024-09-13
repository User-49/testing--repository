def next_num(sequence):
    try:
        next_number = sequence[-1] + sequence[-2]
        return next_number
    except IndexError:
        return 1


sequence = tuple([0])
num = int(input('number of terms in the series: '))
for i in range(num):
    sequence += tuple([next_num(sequence)])
    print(sequence)
