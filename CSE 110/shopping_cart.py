# For my adiition tpo this code, I added a quick one response survey at the end asking how the user's experience was with the program


print('Welcome to your shopping list. ')
print()

cart = []
prices = []
option = int(input("""
 Please select one of the following: 
    1. Add a new item
    2. Display the contents of the shopping cart
    3. Remove an item
    4. Compute the total
    5. Exit 
""" ))


while option != 5 and option != 'Exit':
    if option == 1:
        item = input('\nWhat item do you want to add? ')
        cart.append(item)
        price = float(input(f"\nWhat is the price of this '{item}' ? "))
        prices.append(price)
        print(f"\n'{item}' has been added to the cart. ")

    elif option == 2:
        print("Your cart contains: ")
        for item in range(len(cart)):
            print(f"\n{item+1}. {cart[item]} - ${prices[item]:.2f}")

    elif option == 3:
        for item in range(len(cart)):
            print(f"\n{item+1}. {cart[item]} - ${prices[item]:.2f}")
        remove_item = int(input("\nWhich item do you want to remove? ")) - 1
        del(cart[remove_item])
        del(prices[remove_item])
        print(f"\nItem removed ")

    elif option == 4:
        sum = 0
        for number in prices:
            sum += number
        print(f"\nThe total of all items in cart is $ {sum:.2f}")
    



    option = int(input(f"""
 Please selcet one of the following: 
    1. Add a new item
    2. Display the contents of the shopping cart
    3. Remove an item
    4. Compute the total
    5. Exit 
"""))


else:
    rating = int(input('Ona scale of one to ten, how would you rate the shopping list app? '))
    if rating >= 8:
        print('We are glad that you enjoyed the app. Thank you for your response. Goodbye. ')
    elif rating < 8:
        print('We hope that you have a better experience next time. Thank you for your response. Goodbye. ')
    



    
