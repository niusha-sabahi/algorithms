def insertion_sort(l):
    for n in range(1, len(l)):
        i = n
        while l[i] < l[i-1] and i > 0:              
            l = l[:i-1] + [l[i]] +[l[i-1]] + l[i+1:] 
            i -= 1
    return l

if __name__ == '__main__':
    unsorted = input('Enter a list of numbers to be sorted, separated by comma, or press enter for default [3,8,2,7,5]: ')
    if unsorted == '':
        unsorted = '3,8,2,7,5' 
    unsorted = unsorted.split(',')
    unsorted = [int(x.strip()) for x in unsorted]

    print(insertion_sort(unsorted))