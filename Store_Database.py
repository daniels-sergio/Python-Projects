import sqlite3
from tkinter import *
from tkinter import ttk

# database connection
connection = sqlite3.connect("product_stock.db")
cursor = connection.cursor()

# creates products table if it doesn't exist
cursor.execute("""
  CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    product_name TEXT,
    description TEXT,
    quantity INTEGER,
    price REAL
  );""")

connection.commit()


# uncomment if you wanna delete all records
# cursor.execute("DELETE FROM products;")
# connection.commit()
def add_product():
    global count
    results = cursor.execute("SELECT * FROM products")
    count = 0
    for rows in results:
        count += 1

    # insert products into the database
    cursor.execute("INSERT INTO products (product_name, description, quantity, price) VALUES (?, ?, ?, ?)",
                   (name_entry.get(), description_entry.get(), int(quantity_entry.get()), float(price_entry.get())))
    connection.commit()
    product_id = cursor.lastrowid  # accesses the primary key of the las record
    print(product_id)
    count += 1
    total_label.config(text=f"Total amount of items: {count}")
    # prints what just got added

    print(
        f"Added Record:product_id: {product_id} product_name: {name_entry.get()}, description: {description_entry.get()}, quantity: {quantity_entry.get()}, price: {price_entry.get()}")
    view_all_products()


def delete_product():
    global count
    results = cursor.execute("SELECT * FROM products")
    count = 0
    for rows in results:
        count += 1
    cursor.execute("SELECT * FROM products WHERE product_name = ? AND description = ?;",
                   (name_entry.get(), description_entry.get()))
    result = cursor.fetchone()

    if result:  # checks if the product exists then deletes it
        cursor.execute("DELETE FROM products WHERE product_name = ? AND description = ?;",
                       (name_entry.get(), description_entry.get()))
        connection.commit()

        count -= 1  # Update the count
        print(
            f"Deleted record: product_name: '{name_entry.get()}', description: '{description_entry.get()}', quantity: '{quantity_entry.get()}', price: '{price_entry.get()}'")
    else:
        print("Product not found.")
    view_all_products()


def update_product():
    cursor.execute("SELECT * FROM products WHERE product_name = ? AND description = ?;",
                   (name_entry.get(), description_entry.get()))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE products SET quantity = ?, price = ? WHERE product_name = ? AND description = ?",
                       (int(quantity_entry.get()), float(price_entry.get()), name_entry.get(), description_entry.get()))
        connection.commit()
        print(
            f"Updated record: product_name: '{name_entry.get()}', description: '{description_entry.get()}', quantity: '{quantity_entry.get()}', price: '{price_entry.get()}'")
    else:
        print("Product not found.")
    view_all_products()


def sort_products(order_by, asc=True):
    results_text.delete(1.0, END)
    order = "ASC" if asc else "DESC"
    cursor.execute(f"SELECT * FROM products ORDER BY {order_by} {order}")
    results = cursor.fetchall()
    for row in results:#inserts records into the text box
        results_text.insert(END, f"ID: {row[0]}\n Name: {row[1]}\n Description: {row[2]}\n Quantity: {row[3]}\n Price: {row[4]:.2f}\n_____________________\n")


def view_all_products():
    results_text.delete(1.0, END)
    cursor.execute("SELECT * FROM products") #allows the text box to constantly refresh
    results = cursor.fetchall()
    for row in results:
        results_text.insert(END,f"ID: {row[0]}\n Name: {row[1]}\n Description: {row[2]}\n Quantity: {row[3]}\n Price: {row[4]:.2f}\n_____________________\n")

def sort_product(): #decides what sorting method is gonna occur based on the choice
    selected = sort.get()
    if selected == "Sort by Name Asc":
        sort_products("product_name", True)
    elif selected == "Sort by Name Desc":
         sort_products("product_name", False)
    elif selected == "Sort by Price Asc":
        sort_products("price", True)
    elif selected == "Sort by Price Desc":
        sort_products("price", False)
    elif selected == "Sort by Quantity Asc":
        sort_products("quantity", True)
    elif selected == "Sort by Quantity Desc":
        sort_products("quantity", False)


# GUI setup
window = Tk()
window.geometry("1000x650")
window.title("Inventory Management System")

# input fields
name = Label(window, text="Name: ", font=("Arial", 12, "bold"))
name.place(x=40, y=10)
name_entry = Entry(window, font=("Arial", 12))
name_entry.place(x=160, y=10)

description = Label(window, text="Description: ", font=("Arial", 12, "bold"))
description.place(x=40, y=40)
description_entry = Entry(window, font=("Arial", 12))
description_entry.place(x=160, y=40)

quantity = Label(window, text="Quantity: ", font=("Arial", 12, "bold"))
quantity.place(x=40, y=70)
quantity_entry = Entry(window, font=("Arial", 12))
quantity_entry.place(x=160, y=70)

price = Label(window, text="Price: ", font=("Arial", 12, "bold"))
price.place(x=40, y=100)
price_entry = Entry(window, font=("Arial", 12))
price_entry.place(x=160, y=100)

# buttons


add = Button(window, text="Add Item", command=add_product)
add.pack()
add.place(x=400, y=10)

delete = Button(window, text="Delete Item", command=delete_product)
delete.pack()
delete.place(x=400, y=40)

update = Button(window, text="Update Item", command=update_product)
update.pack()
update.place(x=400, y=70)

sort_label = Label(window,text="Sorting Options: ",font=("Arial", 12, "bold"))
sort_label.pack()
sort_label.place(x=40,y=165)
sort_options = ["Sort by Name Asc", "Sort by Name Desc", "Sort by Price Asc", "Sort by Price Desc", "Sort by Quantity Asc", "Sort by Quantity Desc"]
sort = ttk.Combobox(window,values=sort_options,font=("Aria",12))
sort.place(x=200,y=165)

sort_button = Button(window, text="Sort", command=sort_product)
sort_button.place(x=400, y=165)
results = cursor.execute("SELECT * FROM products")
# text widget for viewing all products
results_text = Text(window, font=("Arial", 10), width=80, height=20)
results_text.pack()
results_text.place(x=200, y=250)

# cursor.execute("DELETE FROM products;")
# connection.commit()
total_label = Label(window, text=f"Total amount of products:", font=('Arial,', 12, 'bold'))
total_label.place(x=36, y=130)

# res = cursor.execute("SELECT product_name FROM products")
# print(res.fetchall())
# main loop
view_all_products()
window.mainloop()

# closes the connection when the program exits
connection.close()
