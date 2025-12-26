# =================================================================
# LIBRARY MANAGEMENT SYSTEM
# Data Structure: List of Dictionaries
# =================================================================

# --- Step 1: Initialize the Data Structure ---
library_inventory = [
    {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "copies": 3},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "copies": 5},
    {"title": "1984", "author": "George Orwell", "copies": 2}
]

# --- Step 2: Implement Input Validation Functions ---

def validate_string_input(prompt):
    """Checks if the user input is not empty (Existence Check)."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ Error: Input cannot be empty. Please try again.")

def validate_positive_integer_input(prompt):
    """Checks for: Existence, Data Type (integer), and Range (positive)."""
    while True:
        try:
            value_str = input(prompt).strip()
            # Check Existence
            if not value_str:
                print("❌ Error: Input cannot be empty. Please try again.")
                continue
                
            # Verify Data Type: Attempt to convert to an integer
            value = int(value_str)
            
            # Validate Range: Ensure it's a positive number (1 or more)
            if value > 0:
                return value
            else:
                print("❌ Error: Number of copies must be a positive integer (1 or more).")
        except ValueError:
            print("❌ Error: Invalid input. Please enter a whole number.")

# --- Step 3: Implement Core Functionalities ---

def display_inventory(inventory):
    """Prints the current list of books and their details."""
    print("\n--- 📚 Current Library Inventory ---")
    if not inventory:
        print("The library currently has no books in the inventory.")
        return

    print(f"Total Unique Books: {len(inventory)}")
    print("-" * 40)
    for i, book in enumerate(inventory, 1):
        print(f"Book {i}:")
        print(f"  Title: {book['title']}")
        print(f"  Author: {book['author']}")
        print(f"  Copies Available: {book['copies']}")
        print("-" * 40)

def add_new_book(inventory):
    """Prompts for book details, validates them, and adds the book to the inventory."""
    print("\n--- ➕ Add New Book ---")
    
    # Get validated string inputs
    title = validate_string_input("Enter the title of the book: ")
    author = validate_string_input("Enter the author's name: ")
    
    # Check if the book already exists
    for book in inventory:
        if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
            print(f"⚠️ Warning: '{title}' by {author} already exists.")
            
            # Offer to add copies to the existing book
            print("Do you want to add more copies to the existing entry? (yes/no): ")
            if validate_string_input("Enter choice: ").lower() == 'yes':
                num_copies = validate_positive_integer_input("Enter the number of copies to add: ")
                book['copies'] += num_copies
                print(f"✅ Success: Added {num_copies} copies. Total copies now: {book['copies']}")
                return
            else:
                print("Returning to main menu without changes.")
                return

    # Get validated positive integer input for new book
    num_copies = validate_positive_integer_input("Enter the number of copies to add: ")

    new_book = {
        "title": title,
        "author": author,
        "copies": num_copies
    }
    inventory.append(new_book)
    print(f"✅ Success: Book '{title}' by {author} added to the inventory with {num_copies} copies.")

def borrow_book(inventory):
    """Prompts for book title, checks availability, and updates the inventory if borrowed."""
    print("\n--- ⬇️ Borrow Book ---")
    
    title_to_borrow = validate_string_input("Enter the title of the book to borrow: ")
    
    # Search for the book
    for book in inventory:
        if book['title'].lower() == title_to_borrow.lower():
            
            # Check if copies are available
            if book['copies'] > 0:
                book['copies'] -= 1
                print(f"✅ Success: You have borrowed '{book['title']}'.")
                print(f"   {book['copies']} copies remaining.")
                return True
            else:
                print(f"⚠️ Sorry, all copies of '{book['title']}' are currently borrowed.")
                return False
    
    # Book not found
    print(f"❌ Error: Book with title '{title_to_borrow}' not found in the inventory.")
    return False

def return_book(inventory):
    """Prompts for book title, finds the book, and increments the copy count."""
    print("\n--- ⬆️ Return Book ---")
    
    title_to_return = validate_string_input("Enter the title of the book to return: ")
    
    # Search for the book
    for book in inventory:
        if book['title'].lower() == title_to_return.lower():
            book['copies'] += 1
            print(f"✅ Success: Thank you for returning '{book['title']}'.")
            print(f"   Total copies now available: {book['copies']}")
            return True
    
    # Book not found
    print(f"❌ Error: Book with title '{title_to_return}' not found in the inventory.")
    print("Please check the title and try again.")
    return False

# --- Step 4: Implement the Main Menu and Execution Loop ---

def main_menu(inventory):
    """Displays the main menu and manages the application flow."""
    while True:
        print("\n" + "="*50)
        print("📖 Welcome to the Library Management System")
        print("="*50)
        print("Please choose an option:")
        print("1. ➕ Add New Book")
        print("2. ⬇️ Borrow Book")
        print("3. ⬆️ Return Book")
        print("4. 📋 Display Inventory")
        print("5. 🚪 Exit")
        print("-" * 50)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_new_book(inventory)
        elif choice == '2':
            borrow_book(inventory)
        elif choice == '3':
            return_book(inventory)
        elif choice == '4':
            display_inventory(inventory)
        elif choice == '5':
            print("\n👋 Thank you for using the Library System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

# --- PROGRAM EXECUTION ---
if __name__ == "__main__":
    main_menu(library_inventory)