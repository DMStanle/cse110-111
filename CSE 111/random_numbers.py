import random

def main():
    numbers = [16.2, 75.1, 52.3]
    return numbers

numbers_list = main()
print(numbers_list)

def append_random_numbers(numbers):
    numbers.append(random.uniform(0, 100))
    numbers_rounded = [round(i, 1) for i in numbers]
    return numbers_rounded

numbers_list = append_random_numbers(numbers_list)
print(numbers_list)

def append_random_numbers(numbers_list, quantity=1):
    for i in range(3):

        numbers_list.append(random.uniform(0, 100))
        numbers_rounded = [round(i, 1) for i in numbers_list]
    return numbers_rounded

numbers_list = append_random_numbers(numbers_list, quantity=1)
print(numbers_list)
if __name__ == "__main__":
    main()