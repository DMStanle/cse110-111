print('Please enter the following information:')
print()
first = input('First name: ')
last = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number: ')
print()
print ('The ID Card is:')
print('--------------------------------------')
print(f'{last.upper() }, {first.capitalize() }')
print(job_title.title() )
print(f'ID:{id_number}')
print()
print(email.lower())
print(phone)
print('--------------------------------------------')