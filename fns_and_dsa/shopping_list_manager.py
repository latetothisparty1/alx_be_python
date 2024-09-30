

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            return shopping_list.append()
        elif choice == '2':
            # Prompt for and remove an item
            return shopping_list.remove()
        elif choice == '3':
            # Display the shopping list
            return shopping_list 
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")