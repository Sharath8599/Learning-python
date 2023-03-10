# Create a function called middle_element that has one parameter named my_list.

#If there are an odd number of elements in my_list, the function should return the middle element. 
#If there are an even number of elements, the function should return the average of the middle two elements.


def middle_element(my_list):
  l=len(my_list)
  if l%2==0:
    sum=my_list[int(l/2 - 1)]+ my_list[int(l/2)]
    avg=sum/2
    return avg
  else:
    return my_list[int(l/2)]


print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 2, -4, 4, 5]))
