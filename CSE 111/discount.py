import datetime

today = datetime.datetime.today()

subtotal = float(input('What is the subtotal? '))

if today.weekday() == 2 or today.weekday() == 3:
    if subtotal >= 50:
        print(f'The subtotal is {subtotal:.2f}')
        discount = subtotal * 0.1
        print(f'The discount is {discount:.2f} ')
        subtotal = subtotal - discount
        tax = subtotal * 0.06
        print(f'The tax is {tax:.2f} ')
        total = subtotal + tax
        print(f'The total is {total:.2f} ')
    else:
        print(f'The subtotal is {subtotal:.2f} ')
        tax = subtotal * 0.06
        print(f'The tax is {tax:.2f} ')
        total = subtotal + tax
        print(f'The total is {total:.2f} ')
else:
    print(f'The subtotal is {subtotal:.2f} ')
    tax = subtotal * 0.06
    print(f'The tax is {tax:.2f} ')
    total = subtotal + tax
    print(f'The total is {total:.2f}')

