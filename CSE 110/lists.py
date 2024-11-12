friends = []

users_friend = ''

while users_friend != 'end':
    users_friend = input('Type the name of a friend: ')
    if users_friend != 'end':
        friends.append(users_friend)


print('Your friends are: ')

for friend in friends:
    print(friend)