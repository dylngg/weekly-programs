import random
import argparse


def main(args):
    parser = argparse.ArgumentParser(description='Sort an Array')
    parser.add_argument('-i', '--items', help='Input for items to be sorted', required=False)
    parser.add_argument('-n', '--length', help='Input for length of array generated (only applicable without -i option)', required=False)
    args = parser.parse_args()
    
    
    if args.items:
        a = args.items.split(',')
        a = [int(item.strip()) for item in a if item is not ' ']
    
    else:
        n = 12
        if args.length and args.length > 1:
            n = int(args.n)
        a = [random.randint(0,n) for i in range(0,n)]
    
    # info about quicksort https://en.wikipedia.org/wiki/Quicksort
    print('Original:')
    print(a, '\nOutcome:')
    
    print(quicksort(a))


def quicksort(a):
    quicksort_recursion(a, 0, len(a) - 1)
    return a


def quicksort_recursion(a, left, right):
    i = left
    j = right
    
    if i < j:
        # choose the middle element
        mid = int((i + j)/2)
        pivot = partition(a, i, j, mid) 
        
        # repeat for both sides
        quicksort_recursion(a, i, pivot -1)
        quicksort_recursion(a, pivot + 1, j)


def partition(a, i, j, index):
    pivot_value = a[index]
    current_index = i
    
    swap(a, index, j)
    for x in range(i, j):
        if a[x] < pivot_value:
            swap(a, x, current_index)
            
            current_index += 1
        
    swap(a, current_index, j)
    return current_index


def swap(a, index1, index2):
    if index1 is not index2:
        temp = a[index1]
        a[index1] = a[index2]
        a[index2] = temp


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
