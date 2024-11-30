from events import EM 
def main():
    manager = EM()
    while True:
        print("\n--- Cultural Fest Management ---")
        print("1. View Events")
        print("2. Add Event")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            manager.display_events()
        elif choice == "2":
            manager.add_event()
        elif choice == "3":
            manager.update_event()
        elif choice == "4":
            manager.delete_event()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
