# Create a function named odd_indices() that has one parameter named lst.

#The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.


def odd_indices(lst):
  new_list=[]
  for i in range(len(lst)):
    if i%2==1:
      new_list.append(lst[i])
      i=i+1
  return new_list



print(odd_indices([4, 3, 7, 10, 11, -2]))
