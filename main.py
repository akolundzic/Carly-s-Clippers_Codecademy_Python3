hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1 create variable 
total_price = 0

# 2 loop through each price
for price in prices:
  print(price)
  total_price += price

# 3 average price
average_price = total_price/len(prices)

# 4 Print average value for one haircut
print(f"average_price: {average_price}")

# 5 list comprehension 
new_prices = [price-5 for price in prices]

# 6 print new price list
print(new_prices)

# 7 create variable total revenue
total_revenue = 0

# 8 get total revenue
for i in range(0,len(hairstyles)):
  # 9 calculate total revenue
  total_revenue += prices[i] * last_week[i]

# 10 total revenue
print(f"Total Revenue : {total_revenue}")

# 11 average daily revenue
average_daily_revenue =  total_revenue/7

# 12 List comprehension
cuts_under_30 = [hairstyles[i]  for i in range(len(hairstyles)) if new_prices[i] < 30 ]

# 13 print all hairstyles under 30 
print(cuts_under_30)





