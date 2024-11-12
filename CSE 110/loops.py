number = float(input('What is a positive number? '))

while number <= 0:
    print('This is not a positive number')
    number = float(input('What is a positive number? '))

print(f'The number is {number}')


answer = ""

while answer != 'yes':
    answer = input('Can I have a cookie? ')

print('Thank you. ')