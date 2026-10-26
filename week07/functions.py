# --- Self-Assessment Questions ---
# 1. The first bug I spotted was the missing colon at the end of line 10. I found it by explaining the code out loud to my lamp. I think this says that my current debugging insticts need a little work so that I can spot bugs instantly, without having to explain it out loud.
# 2. apply_discount(price, tier) is a function that applies a discount to a price given a specific tier. Its inputs are the price and the tier, it returns the discounted price based on the tier. A colleague could not use this without reading the body because they would not know what the function does or what inputs it requires. The function name and parameters give some hints, but without reading the body, they would not know the specific discount rates for each tier.
# 3. No AI used.

# --- Exercise 1 ---

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# --- Exercise 2 ---

# Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price  

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}") # Conditionals are inside the function, functions are inside the loop.

# --- Exercise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax
      
# Calling the final_price function
print(f"After tax: ${final_price(200, 0.07, 'gold'):.2f}")
print(f"final_price(200, 'gold', 0.07): ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

print("="*50)

# --- Exercise 5 ---

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale   # no '+' is a bug. It should be '+=' to accumulate the total.
print(f"Total: ${total}")

count = 0
for sale in sales:  # colon missing is a bug. 
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):   # '=' is a bug. It should be '<' to avoid index out of range error.
    print(sales[i])
    i += 1

print("="*50)

# --- Exercise 6 ---

x = 100

def double_it():
    x = 999 # local x
    return x * 2

print(x)    # 100 prints here because the global variable x is not affected by the local variable x inside the function.
print(double_it())  # 1998 prints here because the function returns the local variable x multiplied by 2.
print(x)    # x is still 100 because the function has its own local variable x, which does not affect the global variable x.