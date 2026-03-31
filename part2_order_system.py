menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

print("\n\n--- Starting Task 1 ---\n")
# 1. Print full menu grouped by category
categories = ["Starters", "Mains", "Desserts"]

for category in categories:
    print("\n===== " + category + " =====")
    
    for item in menu:
        if menu[item]["category"] == category:
            
            price = menu[item]["price"]
            available = menu[item]["available"]
            
            if available == True:
                status = "Available"
            else:
                status = "Unavailable"
            print(f"{item} ₹{price:.2f}   [{status}]")    
            
#2. computations using dictionary methods

# Total number of items on the menu

total_items = len(menu)
print("\nTotal number of items on menu:", total_items)


# Total number of available items

available_count = 0

for item in menu:
    if menu[item]["available"] == True:
        available_count += 1

print("Total available items:", available_count)


# Most expensive item

max_price = 0
max_item = ""

for item in menu:
    price = menu[item]["price"]
    
    if price > max_price:
        max_price = price
        max_item = item

print("Most expensive item:", max_item, "₹", max_price)


# Items priced under ₹150

print("\nItems under ₹150:")

for item in menu:
    price = menu[item]["price"]
    
    if price < 150:
        print(item, "- ₹", price)

print("\n--- Task 1 Completed ---")

print("\n\n--- Starting Task 2 ---\n")
cart = []

# Function to print cart
def print_cart():
    print("\nCurrent Cart:")
    if len(cart) == 0:
        print("Cart is empty")
    else:
        for item in cart:
            print(item)


# 1. Add item to cart
def add_to_cart(item_name, quantity):
    
    if item_name not in menu:
        print(item_name, "does not exist in menu")
        return
    
    if menu[item_name]["available"] == False:
        print(item_name, "is currently unavailable")
        return
    
    price = menu[item_name]["price"]
    
    # check if already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(item_name, "quantity updated in cart")
            return
    
    # if not in cart, add new
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": price
    })
    
    print(item_name, "added to cart")


# 2. Remove item
def remove_from_cart(item_name):
    
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(item_name, "removed from cart")
            return
    
    print(item_name, "not found in cart")


# 3. Update quantity
def update_quantity(item_name, quantity):
    
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = quantity
            print(item_name, "quantity updated")
            return
    
    print(item_name, "not in cart")


# -------- Simulation --------

add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)
print_cart()

add_to_cart("Mystery Burger", 1)
print_cart()

add_to_cart("Chicken Wings", 1)
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()


# -------- Final Order Summary --------

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    name = item["item"]
    qty = item["quantity"]
    price = item["price"]
    
    total = qty * price
    subtotal += total
    
    print(f"{name} x{qty}   ₹{total:.2f}")

print("------------------------------------")

print(f"Subtotal:          ₹{subtotal:.2f}")

gst = subtotal * 0.05
print(f"GST (5%):          ₹{gst:.2f}")

total_payable = subtotal + gst
print(f"Total Payable:     ₹{total_payable:.2f}")

print("====================================")

print("\n--- Task 2 Completed ---")

print("\n\n--- Starting Task 3 ---\n")

import copy

# 1. Create deep copy
inventory_backup = copy.deepcopy(inventory)

print("\nBackup created successfully")


# 2. Change one stock value to test deep copy
inventory["Paneer Tikka"]["stock"] = 2

print("\nChecking deep copy...")
print("Inventory stock:", inventory["Paneer Tikka"]["stock"])
print("Backup stock:", inventory_backup["Paneer Tikka"]["stock"])


# 3. Restore original inventory
inventory = copy.deepcopy(inventory_backup)

print("\nInventory restored")


# -------- Order Fulfilment --------

print("\nUpdating inventory based on cart")

for item in cart:
    
    name = item["item"]
    qty = item["quantity"]
    
    stock = inventory[name]["stock"]
    
    if stock >= qty:
        inventory[name]["stock"] = stock - qty
        print(name, "remaining stock:", inventory[name]["stock"])
    
    else:
        print("Warning:", name, "stock is low")
        inventory[name]["stock"] = 0


# -------- Reorder Alert --------

print("\nReorder Alerts")

for item in inventory:
    
    stock = inventory[item]["stock"]
    reorder = inventory[item]["reorder_level"]
    
    if stock <= reorder:
        print(" Reorder Alert:", item,
              "- Only", stock,
              "left (reorder level:", reorder, ")")


# -------- Final Check --------

print("\nFinal Inventory")
print(inventory)

print("\nInventory Backup")
print(inventory_backup)
print("\n--- Task 3 Completed ---")

print("\n\n--- Starting Task 4 ---\n")
daily_revenue = {}

# 1. Total revenue per day
for date in sales_log:
    
    total = 0
    
    for order in sales_log[date]:
        total = total + order["total"]
    
    daily_revenue[date] = total
    print(date, ":", "₹", total)


# 2. Best selling day

best_day = ""
max_revenue = 0

for date in daily_revenue:
    
    if daily_revenue[date] > max_revenue:
        max_revenue = daily_revenue[date]
        best_day = date

print("\nBest Selling Day:", best_day, "with ₹", max_revenue)


# 3. Most ordered item

item_count = {}

for date in sales_log:
    
    for order in sales_log[date]:
        
        for item in order["items"]:
            
            if item in item_count:
                item_count[item] = item_count[item] + 1
            else:
                item_count[item] = 1


most_item = ""
max_count = 0

for item in item_count:
    
    if item_count[item] > max_count:
        max_count = item_count[item]
        most_item = item

print("\nMost Ordered Item:", most_item, "(", max_count, "orders )")


# 4. Add new day

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nNew day added\n")


# Reprint revenue

print("------ Updated Daily Revenue ------")

daily_revenue = {}

for date in sales_log:
    
    total = 0
    
    for order in sales_log[date]:
        total = total + order["total"]
    
    daily_revenue[date] = total
    print(date, ":", "₹", total)


# Best day again

best_day = ""
max_revenue = 0

for date in daily_revenue:
    
    if daily_revenue[date] > max_revenue:
        max_revenue = daily_revenue[date]
        best_day = date

print("\nUpdated Best Selling Day:", best_day, "with ₹", max_revenue)


# 5. Numbered order list using enumerate

print("\n------ All Orders ------")

all_orders = []

for date in sales_log:
    
    for order in sales_log[date]:
        all_orders.append((date, order))


for number, data in enumerate(all_orders, start=1):
    
    date = data[0]
    order = data[1]
    
    items = ", ".join(order["items"])
    
    print(number, ".", 
          "[", date, "]",
          "Order #", order["order_id"],
          "- ₹", order["total"],
          "- Items:", items)