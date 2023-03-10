# Create a function named double_index that has two parameters: a list named my_list and a single number named index.

#The function should return a new list where all elements are the same as in my_list except for the element at index. The element at index should be double the value of the element at index of the original my_list.

#If index is not a valid index, the function should return the original list.


def double_index(my_list, index):
  if index<len(my_list):
    my_list.insert(index, my_list[index]*2)
    my_list.pop(index+1)
    return my_list
  else:
    return my_list


print(double_index([3, 8, -10, 12], 2))
