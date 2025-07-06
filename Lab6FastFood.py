# Lab 6: Fast Food Functions
# Emily Smith


# Print a welcome message and start building the burger combo
print("Welcome to The Burger Stand!")
print("I'm making your burger combo with cheese, lettuce, and bacon.")


"""Adds ingredients to the burger and prints a message."""
def add_ingredient(ingredient):
    print("Adding " + ingredient + " to your burger!")
add_ingredient("cheese")
add_ingredient("lettuce")
add_ingredient("bacon")

# Constants
TAX_RATE = 0.085
BURGER_PRICE = 4.99
FRIES_PRICE = 2.49
DRINK_PRICE = 1.29

"""Calculates the total price of a burger combo based on selected items.
Returns the total cost and prints a message."""
def calculate_combo_price(has_burger, has_fries, has_drink):
    subtotal = 0
    if has_burger:
        subtotal += BURGER_PRICE
    if has_fries:
        subtotal += FRIES_PRICE
    if has_drink:
        subtotal += DRINK_PRICE

    tax = TAX_RATE * subtotal
    total_cost = subtotal + tax
    print(f"Total combo price: ${total_cost:.2f}")
    return total_cost
calculate_combo_price(True, True, True )

"""Asks the user if they want to supersize their combo.
Returns their order decision and prints a message."""
def order_decision():
    supersize = input("Would you like to supersize your combo?(yes/no): ")
    if supersize.lower() == "yes":
        print("Great choice! Go big or go home!")
        return True
    else:
        print("Remember, life is short, go for the large fries!")
        return False
order_decision()

"""
Using recursion that simulates ordering items from a fast food menu.
The recursion stops when the list is empty.
"""
def order_food(menu):
    if not menu:
        print("Your order is complete. Enjoy your meal!")
        return
    else:
        print("Would you like to order a " +menu.pop(0) + "?")
        input()
        order_food(menu)

menu_items = ["burger", "fries", "drink"]
order_food(menu_items)
