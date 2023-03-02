hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price=0
# for loops
for p in prices:
  total_price+=p

#finding average price of a cut using len() function
average_price= total_price/len(prices)
print(average_price)

#list comprehensions
new_prices=[p-5 for p in prices]
print(new_prices)

total_revenue=0
# using range()
for i in range((len(hairstyles))):
  total_revenue=prices[i]*last_week[i]
print(total_revenue)
# Finding the average daily revenue
average_daily_revenue= total_revenue/7
# using list comprehensions and conditionals
cuts_under_30=[print(hairstyles[i]) for i in range(len(hairstyles)) if new_prices[i]<30]
