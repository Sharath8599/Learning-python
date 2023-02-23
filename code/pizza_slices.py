# Your code below:
toppings=["pepperoni",
"pineapple",
"cheese",
"sausage",
"olives",
"anchovies",
"mushrooms"]

prices=[2,
6,
1,
3,
2,
7,
2]

#Count the number of occurrences of 2 in the prices list
num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)

# length of the toppings
num_pizzas=len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")

# creating a new two-dimensional list
pizza_and_prices=[[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)

# Sorting
pizza_and_prices.sort()

# first element is the cheapest pizza
cheapest_pizza=pizza_and_prices[0]

# lat element is expensive pizza
priciest_pizza=pizza_and_prices[-1]

# a man bought most expensive pizza, now we need to remove that
pizza_and_prices.pop()

# add a new topping
pizza_and_prices.insert(1,[2.5,"peppers"])

# three cheapest pizzas
three_cheapest=pizza_and_prices[0:3]
print(three_cheapest)
