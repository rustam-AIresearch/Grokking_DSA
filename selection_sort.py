my_list = [3,6,5,7,1,10,20]

def findSmallest(list):
    smallest = list[0]
    smallest_index = 0 

    for i in range(len(list) - 1):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index



def selection_sort(list):
    new_list = []
    for i in range(len(list)):
        smallest = findSmallest(list)
        new_list.append(list.pop(smallest))
    return new_list


print(selection_sort([12,9,5,8,19]))