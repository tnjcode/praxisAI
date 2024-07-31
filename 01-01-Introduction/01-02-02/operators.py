a = 5
b = 3

print(a)

a *= 4
print(a)
print("second modul", a%b)

print(a**2)


print("floor division",5//3)
print("division",5/3)
# kalkulator
# # calculator.py

print('''
Please type in the math operation you would like to complete:
+ pertambahan
- pengurangan 
''')

operation = input()

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

else:
    print('You have not typed a valid operator, please run the program again.')