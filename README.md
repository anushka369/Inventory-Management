# Inventory Management System 🏪

## Overview
This Python program is an inventory management system that helps users manage stock levels, process sales, restock items, and track transactions. It uses PyDatalog for logical operations and ensures efficient handling of inventory updates.

---

## Features 🛒
- **View Stock**: Displays all items with their stock levels, prices, and reorder points.
- **Make a Sale**: Deducts stock when an item is sold and logs the transaction.
- **Restock Items**: Increases stock levels for an item and logs the restocking transaction.
- **Total Inventory Value**: Computes the total value of all inventory items.
- **Add New Items**: Allows adding new products to the inventory.
- **Remove Items**: Removes items from the inventory.
- **Low Stock Alerts**: Warns when stock levels fall below the reorder point.
- **Transaction Logging**: Keeps records of all sales and restocking activities.

---

## Installation & Dependencies 📩
Ensure you have Python installed. You also need the following library:
```sh
pip install pyDatalog
```

## Usage 🏹
Run the script and follow the prompts to manage inventory effectively.
```sh
python inventory_management.py
```

---

## Example Operations ⚖
1. **Adding a new item**
   - Enter new item name: `Mango`
   - Enter initial quantity: `30`
   - Enter price per unit: `2.5`
   - Enter reorder point: `10`
   - Output: `Added Mango with quantity 30, price 2.5, and reorder point 10.`

2. **Making a sale**
   - Enter the item name: `Apple`
   - Enter the quantity to sell: `10`
   - Output: `Updated stock for Apple: 40`

3. **Viewing total inventory value**
   - Output: `Total inventory value: $XYZ`

4. **Viewing the transaction log**
   - Output:
     ```
     Sold 10 Apple(s) on 2025-01-29 14:30:00
     Restocked 20 Banana(s) on 2025-01-29 15:00:00
     ```
---

## Future Improvements 📈
- Implement a database backend for persistent storage.
- Add user authentication and role-based access.
- Provide a GUI for a better user experience.

---

## Contributing 🤝

This is a personal learning project, but contributions and suggestions are welcome! 
<br> If you find any improvements, feel free to create a pull request. To contribute:

1. Fork the repository.

2. Create a new branch for your feature/bug fix.

3. Commit your changes and submit a pull request.

---

## 🌷 Author

Developed by **Anushka**. <br>
📧 [ab8991@srmist.edu.in](mailto:ab8991@srmist.edu.in)

---
