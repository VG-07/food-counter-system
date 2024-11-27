# -- User input section
# Enter Product List Size : 4
# Enter Product 1 -
# Samosa
# Enter Product 2 -
# Kachori
# Enter Product 3 -
# Fafda
# Enter Product 4 -
# Jalebi

# Enter Samosa Price :
# 300/-
# Enter Kachori Price :
# 100/-
# Enter Fafda Price :
# 100/-
# Enter Jalebi Price :
# 200/-

# --- output

# samosa = 300
# kachori = 100
# fafda = 100
# jalebi = 200

list =int(input("enter The how many product if you want : "))
food = []
price =  []
for i in range(list):
  list_food = input("enter a List of the food : ")
  food.append(list_food)

for i in food:
  list_price = int(input("enter a price of the product {} :- ".format(i)))
  price.append(list_price)

print("---------------------")

j= 0
for i in range(list):
  print(f'{food[i]} = {price[i]}')

print("-----------------------")
total = 0
for i in range(len(price)):
   total = total+price[i]
print("Total proce of the product:  ",total)