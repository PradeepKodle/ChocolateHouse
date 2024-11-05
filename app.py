
import sqlite3
from datetime import datetime

DATABASE_PATH = "database/chocolate_house.db"

def connect_db():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

# Manage Seasonal Flavors
def add_seasonal_flavor(name, available_from, available_until):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO seasonal_flavors (name, available_from, available_until) VALUES (?, ?, ?)",
        (name, available_from, available_until)
    )
    conn.commit()
    conn.close()

# Manage Ingredient Inventory
def add_ingredient(ingredient_name, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)",
        (ingredient_name, quantity)
    )
    conn.commit()
    conn.close()

# Customer Suggestions
def add_customer_suggestion(customer_name, flavor_suggestion, allergy_concerns):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)",
        (customer_name, flavor_suggestion, allergy_concerns)
    )
    conn.commit()
    conn.close()

# CLI Interface
def main():
    print("Chocolate House Management System")
    while True:
        print("\n1. Add Seasonal Flavor\n2. Add Ingredient\n3. Add Customer Suggestion\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Flavor Name: ")
            available_from = input("Available From (YYYY-MM-DD): ")
            available_until = input("Available Until (YYYY-MM-DD): ")
            add_seasonal_flavor(name, available_from, available_until)
        elif choice == '2':
            ingredient = input("Ingredient Name: ")
            quantity = int(input("Quantity: "))
            add_ingredient(ingredient, quantity)
        elif choice == '3':
            customer_name = input("Customer Name: ")
            suggestion = input("Flavor Suggestion: ")
            allergy = input("Allergy Concerns: ")
            add_customer_suggestion(customer_name, suggestion, allergy)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
