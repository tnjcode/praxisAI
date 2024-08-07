# print ("masukan nomor")
# x = input()
# print("X")
# y = input()
# print("result: ",int(x)*int(y))

print('''
Please type in the math operation you would like to complete:
+ pertambahan
- pengurangan 
''')

operation = input()

# mengubah string menjadi integer supaya bisa melakukan operasi matematika
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