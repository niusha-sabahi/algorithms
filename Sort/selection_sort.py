# Time Complexity : O(n^2)
# min function is a for loop itself

def selection_sort(l):
    for i in range(0, len(l)):
        if l[i] > min(l):
            i_min = l.index(min(l[i:]))
            l[i], l[i_min] = l[i_min], l[i]
    return l

if __name__ == '__main__':
    unsorted = input('Enter a list of numbers to be sorted, separated by comma, or press enter for default [3,8,2,7,5]: ')
    if unsorted == '':
        unsorted = '3,8,2,7,5' 
    unsorted = unsorted.split(',')
    unsorted = [int(x.strip()) for x in unsorted]

    print(selection_sort(unsorted))