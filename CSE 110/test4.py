with open('courses.txt') as courses_file:
    for line in courses_file:
        parts = line.split(',')
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3


        print(f'{name} Grade: {grade}, after bonus: {bonus_grade}')

