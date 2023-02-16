weight=1.5
#Ground Shipping
if weight<=2:
  cost_ground=weight*1.50 + 20
elif weight>2 and weight<=6:
  cost_ground=weight*3.00 + 20
elif weight>6 and weight<=10:
  cost_ground=weight*4.00 + 20
else:
  cost_ground=weight*4.75 + 20
print("Cost of ground shipping is $",cost_ground)

# Ground Shipping Premium
cost_of_premium_ground = 125
print("Cost of premium ground shipping is $",cost_of_premium_ground)

# Drone Shipping
if weight<=2:
  cost_drone=weight*4.50
elif weight>2 and weight<=6:
  cost_drone=weight*9.00
elif weight>6 and weight<=10:
  cost_drone=weight*12.00
else:
  cost_drone=weight*14.75
print("Cost of Drone Shipping is $",cost_drone)
