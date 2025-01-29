from pyDatalog import pyDatalog

# Initialize PyDatalog
pyDatalog.create_terms('Item, Quantity, Price, ReorderPoint, StockLevel, '
                       'TotalInventoryValue, update_stock, sale, restock, add_item, '
                       'remove_item, log_transaction, X')

# Define inventory items with their respective quantities, prices, and reorder points
+Item['Apple'] == (50, 1.5, 20)
+Item['Banana'] == (100, 0.5, 30)
+Item['Orange'] == (80, 2.0, 25)

# Transaction log
transaction_log = []

# Function to add a new item to inventory
def add_item(item, quantity, price, reorder_point):
    if item in Item.data:
        print(f"{item} already exists in inventory.")

    else:
        +Item[item] == (quantity, price, reorder_point)
        print(f"{item} added to inventory.")

# Function to remove an item from inventory
def remove_item(item):
    if item in Item.data:
        del Item.data[item]
        print(f"{item} removed from inventory.")

    else:
        print(f"{item} not found in inventory.")

# Function to update stock levels
def update_stock(item, new_quantity):
    if item in Item.data:
        old_qty, price, reorder_point = Item.data[item]
        new_qty = old_qty + new_quantity
        +Item[item] == (new_qty, price, reorder_point)  # Updating the quantity
        return new_qty
    return "Item not found."

# Function to process sales
def sale(item, sold_quantity):
    if item in Item.data:
        old_qty, price, reorder_point = Item.data[item]
        if old_qty >= sold_quantity:
            new_qty = old_qty - sold_quantity
            +Item[item] == (new_qty, price, reorder_point)
            transaction_log.append(f"Sold {sold_quantity} of {item}")
            return new_qty
        return "Not enough stock."
    return "Item not found."

# Function to restock items
def restock(item, restock_quantity):
    if item in Item.data:
        old_qty, price, reorder_point = Item.data[item]
        new_qty = old_qty + restock_quantity
        +Item[item] == (new_qty, price, reorder_point)
        transaction_log.append(f"Restocked {restock_quantity} of {item}")
        return new_qty
    return "Item not found."

# Calculate total inventory value
def calculate_inventory_value():
    return sum(Item.data[item][0] * Item.data[item][1] for item in Item.data)

# Function to check stock levels
def check_stock():
    low_stock_items = [item for item in Item.data if Item.data[item][0] <= Item.data[item][2]]
    if low_stock_items:
        print("⚠️ Low stock alert for:", ", ".join(low_stock_items))
    return low_stock_items

# User inputs for simulating sales and restocking transactions
while True:
    print("\nChoose an operation:")
    print("1. View stock")
    print("2. Make a sale")
    print("3. Restock items")
    print("4. View total inventory value")
    print("5. Add new item")
    print("6. Remove an item")
    print("7. View transaction log")
    print("8. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        for item in Item.data:
            qty, price, reorder_point = Item.data[item]
            print(f"Item: {item}, Stock: {qty}, Price: {price}, Reorder Point: {reorder_point}")
        check_stock()

    elif choice == 2:
        item = input("Enter the item name: ")
        sold_qty = int(input(f"Enter the quantity to sell of {item}: "))
        result = sale(item, sold_qty)
        print(result)

    elif choice == 3:
        item = input("Enter the item name: ")
        restock_qty = int(input(f"Enter the quantity to restock for {item}: "))
        result = restock(item, restock_qty)
        print(result)

    elif choice == 4:
        inventory_value = calculate_inventory_value()
        print(f"Total inventory value: {inventory_value}")

    elif choice == 5:
        item = input("Enter new item name: ")
        quantity = int(input("Enter initial quantity: "))
        price = float(input("Enter price per unit: "))
        reorder_point = int(input("Enter reorder point: "))
        add_item(item, quantity, price, reorder_point)

    elif choice == 6:
        item = input("Enter the item name to remove: ")
        remove_item(item)

    elif choice == 7:
        print("\nTransaction Log:")
        for log in transaction_log:
            print(log)

    elif choice == 8:
        break

    else:
        print("Invalid choice. Try again.")
