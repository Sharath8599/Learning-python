# Write a function named combine_sort that has two parameters named my_list1 and my_list2.

#The function should combine these two lists into one new list and sort the result. Return the new sorted list.

def combine_sort(my_list1, my_list2):
  l=my_list1+my_list2
  sl=sorted(l)
  return sl


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
