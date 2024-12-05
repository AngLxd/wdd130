def display_menu():
    """Displays the main menu options to the user."""
    print("\nHello, welcome to your shopping cart. Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Quit")

def main():
    """Main function for the Shopping Cart Program."""
    print("Welcome to the Shopping Cart Program!")
    
    # List to store all the item names
    cart = []
    
    while True:
        display_menu()  # Displays the menu

        choice = input("Please enter an action: ") # Get the user's choice
        if choice == "1":
            item = input("What item would you like to add? ") # Type to add an item to the cart
            cart.append(item)
            print(f"'{item}' has been added to the cart.") #Shows new item in cart if option "2" is selected
        elif choice == "2":
            if cart:
                print("The contents of the shopping cart are:") #shows all items that have been added
                for item in cart:
                    print(f"- {item}")
            else:
                print("Your cart is empty.") #if no item has been added it will display this message
        elif choice == "3":
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() #starts the program but waiting for the user's input to start other task
