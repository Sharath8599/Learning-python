# Write a function named first_three_multiples() that has one parameter named num.

# This function should print the first three multiples of num. Then, it should return the third multiple.

def first_three_multiples(num):
  print(num*1, num*2, num*3)
  return num*3


first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
