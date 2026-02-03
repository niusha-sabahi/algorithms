def linear_search(list, key):
    for i in range(0, len(list)):
        if list[i] == key:
            return i
    return -1

if __name__ == '__main__':
    list = input('Enter a list of numbers, separated by comma, or press enter for default 3,8,6,7,9,5,1,8,4: ')
    if list == '':
        list = '3,8,6,7,9,5,1,8,4'
    list = list.split(',')
    list = [int(x.strip()) for x in list]

    key = input("Enter the number you wish to search for, or press enter for default '1': ")
    if key == '':
        key = '1'
    key = int(key)

    print(linear_search(list, key))