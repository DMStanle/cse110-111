#courses_file = open('courses.txt') "Not needed because of line 3"


with open('courses.txt') as courses_file:
    for line in courses_file:
        print(line)



