import math

def main():

    pass



def compute_volume(radius, height):

    volume = radius**2
    volume2 = math.pi * volume
    volume3 = volume2 * height

    return volume3

def compute_surface_area(radius, height):

    sa = radius + height
    sa2 = 2 * math.pi
    sa3 = sa2 * radius
    sa4 = sa3 * sa

    return sa4




volume = compute_volume(6.83, 10.16)

surface_area = compute_surface_area(6.83, 10.16)

storage_efficiency = volume / surface_area

print(storage_efficiency)






























main()