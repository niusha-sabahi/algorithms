import math
# Does not work - needs implementation, test written

# def partitioner(l):

#     return left_l, right_l

def quick_sort(l):
    med_i = math.floor(len(l)/2)
    left_l = []
    right_l = []
    for i in range(0, len(l)):
        if l[i] <= l[med_i]:
            left_l.append(l[i])
        elif i != med_i:
            right_l.append(l[i])
    print(med_i)
    print(left_l)
    print(right_l)

    return [quick_sort(left_l) + quick_sort(right_l)]
    

if __name__ == '__main__':
    unsorted = input('Enter a list of numbers to be sorted, separated by comma, or press enter for default [3,8,2,7,5]: ')
    if unsorted == '':
        unsorted = '3,8,2,7,5' 
    unsorted = unsorted.split(',')
    unsorted = [int(x.strip()) for x in unsorted]

    print(quick_sort(unsorted))