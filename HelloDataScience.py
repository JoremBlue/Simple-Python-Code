print("Hello, Data Science!")



score = int(input("Enter your test score: "))
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good job")
else:
    print("Keep practicing")


for i in range(1, 6):
    print("Number:", i)



def greet(name):
    return "Hello, " + name + "!"

print(greet("Jorem Blue"))



def calculate_total(prices):
    return sum(prices)

def apply_discount(total):
    if total > 500:
        return total * 0.10
    else:
        return 0

def display_receipt(items, prices, total, discount):
    print("\nReceipt")
    print("-" * 30)
    for name, price in zip(items, prices):
        print(f"{name}: ₱{price:.2f}")
    print("-" * 30)
    print(f"Total before discount: ₱{total:.2f}")
    print(f"Discount: ₱{discount:.2f}")
    print(f"Amount to Pay: ₱{total - discount:.2f}")
    print("-" * 30)

items = []
prices = []

num_items = int(input("How many items do you want to buy? "))

for i in range(num_items):
    name = input(f"Enter name of item {i+1}: ")
    price = float(input(f"Enter price of item {i+1}: ₱"))
    items.append(name)
    prices.append(price)

total = calculate_total(prices)
discount = apply_discount(total)
display_receipt(items, prices, total, discount)
