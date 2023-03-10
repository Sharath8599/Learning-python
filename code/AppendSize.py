# Create a function called append_size that has one parameter named my_list.

#The function should append the size of my_list (inclusive) to the end of my_list. The function should then return this new list.


def append_size(my_list):
   a= len(my_list)
   my_list.append(a)
   return my_list
   

print(append_size([23, 42, 108]))
