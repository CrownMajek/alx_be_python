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
            choice = input("Enter the item to add: ")
            choice = shopping_list.append(choice)
            # Prompt for and add an item
        elif choice == '2':
            choice = input("Enter the name of the item: ")
            if choice not in shopping_list:
                print(f"{choice} not found")
            else:
                choice = shopping_list.remove(choice)
            # Prompt for and remove an item
        elif choice == '3':
            print(shopping_list)
            # Display the shopping list
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()   

