# Reflection Questions:
# 1. Coming in with no coding experience, I didn’t have expectations, but what surprised me most was how easily lists can be changed. In Exercise 5, I changed a value in a list with no error at all, and only when I switched to a tuple did Python stop me. It showed me that the difference between brackets and parentheses really matters.
# 2. As an office assistant at my old school, I had to sort student files by whether or not they had a referral. I did it by hand, which took an entire day because there were so many files. If I had put the names in a Python list, I could have written a short loop that checked each one and automatically sorted them into two lists, ‘referral’ and ‘no referral.’ In Excel, I would have had to filter and copy rows manually each time new files came in, but with Python I could have just rerun the code.

# Exercise 1: Building a list

print("---Exercise 1: Build a List ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item (not hard coded)

print("--- Exercise 3: List slicing ---")

print(inventory[:3]) # grabs the first three items
print(inventory[-2:]) # grabs the last two items
print(inventory[::2])


print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # adds an item to the end of the list
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort() # sorts the list in alphabetical order
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) # New York City coordinates

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")

print(coords)

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f"Number of Sales: {count}")
print(f"Average Sales: {average}")
print(f"Best Sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")




