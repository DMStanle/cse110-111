import random

def main():
    numbers = []
    for i in range(3):
        numbers.append(random.uniform(0, 100))
    rounded_numbers = [round(i, 1) for i in numbers]
    return rounded_numbers

numbers_list = main()

print(numbers_list)

def append_random_numbers(numbers_list):
    numbers_list.append(random.uniform(1, 100))
    numbers_list_rounded = [round(i, 1) for i in numbers_list]
    return numbers_list_rounded

new_numbers_list = append_random_numbers(numbers_list)

print(new_numbers_list)


if __name__ == "__main__":
    main()
