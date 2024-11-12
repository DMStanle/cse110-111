max_year = 0
max_country = ''
max = 0
min_year = 0
min_country = ''
min = 1000000

age_list = []
specific_min_age = 1000000
specific_min_country = ''
specific_max_age = 0
specific_max_country = ''

chosen_year = int(input('What year wouldyou like info on? '))
with open('life-expectancy.csv') as life:
    for i, line in enumerate(life):
        if i == 0:
            continue
        line = line.strip()
        data = line.split(',')
        country = data[0]
        year = int(data[2])
        age = float(data[3])

        if age > max:
            max = age
            max_country = country
            max_year = year



        if age < min:
                min = age
                min_country = country
                min_year = year


        if year == chosen_year:
            age_list.append(age)

            if age < specific_min_age:
                specific_min_age = age
                specific_min_country = country
            if age > specific_max_age:
                specific_max_age = age
                specific_max_country = country







            


average = sum(age_list) / len(age_list)
print(f'')
print()
print(f'Overall maximum life expectancy is: {max} from {max_country} in {max_year}')
print(f'Overal minimum life expectancy is: {min} from {min_country} in {min_year} ')
print()
print(f'In {chosen_year}: ')
print(f'Life expectancy on average was {average:.2f} ')
print(f'Maximum life expectancy was from {specific_max_country} with {specific_max_age}')
print(f'The minimum life expectancy was from {specific_min_country} with {specific_min_age}')



        

        




        