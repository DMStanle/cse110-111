total_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per  box: '))

import math

boxes_needed = total_items / items_per_box

print(f'For {total_items} items, packing {items_per_box} items in each box, you will need {math.ceil(boxes_needed)} boxes. ')

