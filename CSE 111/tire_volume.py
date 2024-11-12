import math
from datetime import datetime

width = float(input('What is the width of the tire in mm (ex 205): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel inn inches (ex 15): '))

volume = width * aspect_ratio
volume += 2540 * diameter
volume2 = width**2
volume3 = math.pi * volume2
volume4 = volume3 * aspect_ratio
volume5 = volume4 * volume

final_volume = volume5 / 10000000000

print(f'The appoximate volume is {final_volume:.2f} liters')

if diameter > 11 and diameter <= 15:
    print('Expect to spend from $80 to $150')
elif diameter > 15 and diameter <= 20:
    print('Expect to spend from $100 to $400')
elif diameter > 20:
    print('Expect to spend from $200 to $1000')

current_date = datetime.now()

with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f} ,{final_volume:.2f}", file=volumes_file)



 

