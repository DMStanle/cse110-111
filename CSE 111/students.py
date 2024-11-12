import csv

def main():

    INUMBER_INDEX = 0
    NAME_INDEX = 1



    students_dict = read_dictionary('students.csv', INUMBER_INDEX)
    print(students_dict)

    selected_student = input('Please enter an I-number: ')

    if selected_student in students_dict:
        value = students_dict[selected_student]
        name = value[NAME_INDEX]
        print(name)
    else:
        print('No such student.')

def read_dictionary(students, key_column_index):

    dictionary = {}

    with open(students, 'rt') as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:

                key = row_list[key_column_index]

                dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()