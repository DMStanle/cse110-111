

def main():
    text_list = read_list('provinces.txt')
    print(text_list)

    text_list.pop(0)
    text_list.pop()

    count = 0


    for i in range(len(text_list)):
        if text_list[i] == 'AB':
            text_list[i] = 'Alberta'
    
        if text_list[i] == 'Alberta':
            count += 1
        
    print(f'The number of times "Alberta" is in the list is {count}.')

    


    





def read_list(provinces):
    text_list = []

    with open(provinces, 'rt') as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
        return text_list
    

if __name__ == "__main__":
    main()