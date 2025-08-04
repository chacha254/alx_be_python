def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("add item")
            shopping_list.append(input("Add items to list:")) 
            print(shopping_list)
            # Prompt for and add an item
            pass
        elif choice == '2':
            print("Remove item")
            shopping_list.remove(input("remove item from list:"))
            for items in shopping_list:
                if input != shopping_list:
                    print("item not on shopping list")
                else:
                    print(shopping_list)
            # Prompt for and remove an item
            pass
        elif choice == '3':
            print(shopping_list)
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()