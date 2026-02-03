import math

def binary_search_recursive(list_start, list_end, list, key):
    active_list = list[list_start:list_end+1]
    mid = math.floor((len(active_list)-1)/2) + list_start
    if list[mid] == key:
        return mid
    elif list_end-list_start <= 0:
        return -1
    elif key > list[mid]:
        list_start = mid+1
        return binary_search_recursive(list_start, list_end, list, key)
    elif key < list[mid]:
        list_end = mid-1
        return binary_search_recursive(list_start, list_end, list, key)

def binary_search_iterative(list, key):
    list_start = 0
    list_end = len(list)-1
    while list_end-list_start >= 0:
        active_list = list[list_start:list_end+1]
        mid = math.floor((len(active_list)-1)/2) + list_start
        if list[mid] == key:
            return mid
        elif key > list[mid]:
            list_start = mid+1
        elif key < list[mid]:
            list_end = mid-1
    return -1

if __name__ == '__main__':
    list = input('Enter a list of numbers, separated by comma, or press enter for default [3,8,6,7,9,5,1,8,4]: ')
    if list == '':
        list = '3,8,6,7,9,5,1,8,4'
    list = list.split(',')
    list = [int(x.strip()) for x in list]
    list = sorted(list)

    key = input("Enter the number you wish to search for, or press enter for default '3': ")
    if key == '':
        key = '3'
    key = int(key)

    it_or_re = input('I: Iterative\nR: Recursive\nEnter selected method: ')

    if it_or_re == 'I':
        result = binary_search_iterative(list, key)
    elif it_or_re == 'R':
        result = binary_search_recursive(0, len(list)-1, list, key)

    print('Result is : ', result)
