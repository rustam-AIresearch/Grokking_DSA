# Binary Search - Introduction
def binary_search(list,item):
    low = 0 
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1 ### towards left side

        else: 
            low = mid + 1  ## towards  right side

    return None 


my_list = [0,2,4,6,8,10]


print(f'Your value locate in {binary_search(my_list, 6)}')
print('Function completed')