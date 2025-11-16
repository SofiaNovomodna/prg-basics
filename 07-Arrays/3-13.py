#Define a function occurs(number, array) that returns True if a given number is present in an array. Then create a program that checks whether the number entered from the keyboard is present in the array [15, 38, 7, 23, 14]. Sample result:

#Number: 23
#Array: 15 38 7 23 14
#Result: number 23 appears in the array

def occurs(array):
    number = input('Number: ')
    print('Array:', end= ' ')
    for i in array:
        print(i, end= ' ')
    print()
    print('Result:', end= ' ')
    if int(number) in array:
        print(f'number {number} appears in the array')
    else:
        print(f'number {number} does not appear in the array')

occurs([15, 38, 7, 23, 14])