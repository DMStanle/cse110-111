shopping_cart = [
    ['chips', 2.99],
    ['Bread', 2.50],
    ['Milk', 3.19],
    ['Ice Cream', 6.99],
    ['Cheese', 5.99],
    ['Candy Bar', 0.99]
]

max_price = -1
max_product = ''

for item in shopping_cart:
    product_name = item[0]
    price = item[1]

    if price > max_price:

        max_price = price

        max_product = product_name

print(f'The max price is: {max_price}')
print(f'The product with the highest price is: {max_product}')


