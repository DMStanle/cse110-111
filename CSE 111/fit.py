import csv

def main():

   weight = float(input('What is your current weight(lbs)? ')) * 0.454
   gender_lower = input('What is your gender?("m" or "f") ')
   height = float(input('What is your height in inches? ')) * 2.54
   age = float(input('What is your age in years? '))
   gender = gender_lower.upper()
   
   bmr = calculate_bmr(gender, weight, height, age)
   print(f'Your BMR is {bmr:.0f} calories/day.')

   goal_lower = input('Do you want to gain weight or lose weight(Respond with "gain" or "lose")? ')
   goal = goal_lower.upper()
   exercise = int(input('How many days a week do you exercise(Respond with a number between 0 and 7)? '))

   daily_calories = get_daily_calories(bmr, goal, exercise)

   print(f'You should consume {daily_calories:.0f} calories each day.')

   text_list = read_file('weight_loss.txt', 'weight_gain.txt', goal)

   print()
   print('Here are some tips for what you want to achieve: ')
   print()

   for line in text_list:
       print(line)
    
   NAME_INDEX = 0
   HEIGHT_INDEX = 1
   WEIGHT_INDEX = 2
   ROLE_INDEX = 3
   CALORIES_INDEX = 4
   DAYS_INDEX = 5


   celebrities_dict = celebrities('celeb.csv', NAME_INDEX )

   print()
   print('Do you want to look like one of the following celebrities? Henry Cavill, Chris Hemsworth, Chris Pratt, Christian Bale, Scarlett Johansson, Gal Gadot, Alexandra Daddario, Margot Robbie.')
   print()

   selected_celebrity = input('Please enter the name of the celebrity that you would like to look like: ')

   if selected_celebrity in celebrities_dict:
       value = celebrities_dict[selected_celebrity]
       name = value[NAME_INDEX]
       height2 = value[HEIGHT_INDEX]
       weight2 = value[WEIGHT_INDEX]
       role = value[ROLE_INDEX]
       calories = value[CALORIES_INDEX]
       days = value[DAYS_INDEX]
       print(f'{name} was {height2}" & {weight2} pounds for the role of {role}, and consumed {calories} calories per day while exercising {days} days per week. ')
   else:
       print('Celebrity not in list.')

    




    
    



def calculate_bmr(gender, weight, height, age):
    if gender == 'M':
        bmr1 = 10 * weight
        bmr2 = 6.25 * height
        bmr3 = 5 * age
        bmr4 = bmr1 + bmr2 - bmr3 + 5
    elif gender == 'F':
        bmr1 = 10 * weight
        bmr2 = 6.25 * height
        bmr3 = 5 * age
        bmr4 = bmr1 + bmr2 - bmr3 - 161

    return bmr4

def get_daily_calories(bmr, goal, exercise):
    none_list = [0]
    little_list = [1, 2]
    moderate_list = [3, 4, 5]
    high_list = [6, 7]
    if goal == 'GAIN':
        if exercise in none_list:
            calories = bmr * 1.2 + 300
        elif exercise in little_list:
            calories = bmr * 1.375 + 300
        elif exercise in moderate_list:
            calories = bmr * 1.55 + 300
        elif exercise in high_list:
            calories = bmr * 1.725 + 300
    elif goal == 'LOSE':
           if exercise in none_list:
            calories = bmr * 1.2 - 300
           elif exercise in little_list:
               calories = bmr * 1.375 - 300
           elif exercise in moderate_list:
               calories = bmr * 1.55 - 300
           elif exercise in high_list:
               calories = bmr * 1.725 - 300
    return calories


def read_file(weigth_loss, weight_gain, goal):
    text_list = []
    if goal == 'GAIN':
        with open(weight_gain, 'rt') as file:
            for line in file:
                clean_line = line.strip()
                text_list.append(clean_line)
    elif goal == 'LOSE':
        with open(weigth_loss, 'rt') as file:
            for line in file:
                clean_line = line.strip()
                text_list.append(clean_line)
    return text_list

def celebrities(celeb, key_column_index):
    dictionary = {}
    with open(celeb, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for i in reader:
            if len(i) != 0:
                key = i[key_column_index]
                dictionary[key] = i
    return dictionary






if __name__ == "__main__":
    main()