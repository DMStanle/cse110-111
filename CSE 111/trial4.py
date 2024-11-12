from array import array

# LIST

#names = ['Chris', 'Susan']
#scores = []
#scores.append(98)
#scores.append(99)
#print(names)
#print(scores)
#print(scores[1])

#ARRAY

scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

print()

names = ['Susan', 'Josiah', 'Andre', 'Chris']
print(len(names)) #Get number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort()
print(names)

presenters = names[ :3]
print(names)
print(presenters)

#Dictionary

person = {'first': 'Chris'}
person['last'] = 'Harrison'
print(person)
print(person['first'])

#Loops

for name in ['Chris', 'Susan']:
    print(name)


for index in range(0, 2):
    print(index)


names = ['Chris', 'Susan']
index = 0
while index < len(names):
    print(names[index])
    index = index + 1 

# Example 5
def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]
    # Use a for loop to print each element in the list.
    #Most people prefer this next one to the later one.
    for color in colors:
        print(color)
    print()
    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        # Use the index i to retrieve
        # an element from the list.
        color = colors[i]
        print(color)
# Call main to start this program.
if __name__ == "__main__":
    main()