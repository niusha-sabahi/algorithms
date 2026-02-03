#TODO needs optimisation to skip unecessary passes

def bubble_sort(l):
    for j in range(0, len(l)):
        for i in range(0, len(l) - 1):
            num1 = l[i]
            num2 = l[i+1]
            if num1 > num2:
                l[i] = num2
                l[i+1] = num1
    return l

if __name__ == '__main__':
    unsorted = input('Enter a list of numbers to be sorted, separated by comma, or press enter for default [3,8,2,7]: ')
    if unsorted == '':
        unsorted = '3,8,2,7' 
    unsorted = unsorted.split(',')
    unsorted = [int(x.strip()) for x in unsorted]

    print(bubble_sort(unsorted))