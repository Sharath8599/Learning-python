# Write a function named append_sum that has one parameter — a list named named my_list.

#The function should add the last two elements of my_list together and append the result to my_list. 
#It should do this process three times and then return my_list.

def append_sum(my_list):
  my_list.append(my_list[-1]+my_list[-2])
  my_list.append(my_list[-1]+my_list[-2])
  my_list.append(my_list[-1]+my_list[-2])
  return my_list


print(append_sum([1, 1, 2]))
