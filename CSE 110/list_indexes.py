print('Please enter the items of the shopping list (Type "quit" to fishish): ')

shopping_list = []

item = ''


while item != 'quit':
    item = input('Item: ')

    if item != 'quit':
        shopping_list.append(item)

print('The shopping list is: ')
for item in shopping_list:
    print(item)

print('The shopping list with indexes is: ')
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')

index = int(input('Which item would you liike to change? '))
new_item = input('What is the new item? ')

shopping_list[index] = new_item

print('The shopping list with indexes is now: ')
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')
