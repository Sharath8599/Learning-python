statement_one = False

statement_two = True

credits = 120
gpa = 3.4

if credits >= 120 and gpa>=2.0:
  print("You meet the requirements to graduate!")
if credits>=120 or gpa>=2.0:
  print("You have met at least one of the requirements.")
if not credits>=120:
  print("You do not have enough credits to graduate.")
if not gpa>=2.0:
  print("Your GPA is not high enough to graduate.")
