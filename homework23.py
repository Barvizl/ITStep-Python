# Homework

# Task 4
def print_formatted_text():

    print('"Don\'t compare yourself with anyone in this world...\nif you do so, you are insulting yourself."\nBill Gates')

print_formatted_text()

# Task 5
def even_numbers_in_range(a: int, b: int):

    for even_num in range(a, b+1):
        if even_num % 2 == 0:
            print(even_num, end=' ')
        else:
            continue

a = int(input('Enter a number: '))
b = int(input(('Enter b number: ')))
even_numbers_in_range(a, b)

# Task 6
def print_square(a: int, symbol: str, occupancy: bool):

    if occupancy:
        for column in range(a):
            for row in range(a):
                print(symbol, sep='', end='  ')
            print()
    else:
        space = '   '

        for row1 in range(a):
            print(' ', symbol, sep='', end='  ')
        
        for rows in range(a-1):
            print('\n ', symbol, (a)*space, symbol, sep='', end=' ')
        print()

        for row2 in range(a):
            print(' ', symbol, sep='', end='  ')



a = int(input('Enter a side of a square: '))
symbol = input('Enter the symbol to build a square: ')
occupancy = bool(input('Will it be filled(True) or not(ENTER): '))

print_square(a, symbol, occupancy)

# Task 7
def min_number_from_numbers(array: list) -> int:

    min_number = array[0]
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            min_number = array[i]
        else:
            continue

    return min_number

array = []
for number in range(5):
    array.append(int(input(f'Enter number #{number+1}: ')))

print(min_number_from_numbers(array))


# Task 8
def multiply_in_range(a: int, b: int) -> int:

    result = 1

    if a < b:
        for multiply in range(a, b+1):
            result *= multiply
    elif a > b:
        for multiply in range(b, a+1):
            result *= multiply
    else:
        result = a
    
    return result

a = int(input('Enter a number: '))
b = int(input('Enter b number: '))

print(multiply_in_range(a, b))

# Task 9
def digits_counter(a: int) -> int:

    a = str(a)
    return len(a)

a = int(input('Enter a number: '))
print(digits_counter(a))

# Task 10
def is_palindrom(a: int) -> bool:
    
    a = str(a)

    if a[0] == a[-1] and a[1] == a[-2]:
        return True
    else: 
        return False

a = int(input('Enter 5-digits number: '))

if  a > 9999 and a < 100000:
    print(is_palindrom(a))
else:
    print('INVALID NUMBER. You can enter only 5-digits number')
