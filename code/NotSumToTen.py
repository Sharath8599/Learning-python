#Create a function named not_sum_to_ten() that has two parameters named num1 and num2.

#Return True if num1 and num2 do not sum to 10. Return False otherwise.

# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
  if (num1 + num2 != 10):
    return True
  else:
    return False
  

print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False
