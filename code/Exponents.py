# Create a function named exponents() that takes two lists as parameters named bases and powers. 
# Return a new list containing every number in bases raised to every number in powers


def exponents(bases,powers):
  new_list=[]
  for i in bases:
    for j in powers:
      new_list.append(i**j)
  return new_list


print(exponents([2, 3, 4], [1, 2, 3]))
