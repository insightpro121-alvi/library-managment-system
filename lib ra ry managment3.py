# Library Inventory Management System 

def add_book(book_dict):
    while True:
        book_id = input("Enter Book ID: ")
        if book_id in book_dict:
            print("Book already exists.")
        else:
            # Book details
            book_name = input("Enter book name: ")
            author_name = input("Enter author name: ")
            year_published = input("Enter year: ")
            status = "available"

            # Add book to dictionary
            book_dict[book_id] = {
                "Title": book_name,
                "Author": author_name,
                "Year": year_published,
                "Status": status
            }
            print("\nBook added successfully!")

        # Ask if user wants to add more books
        cont = input("Do you want to add more books (y/n): ").lower()
        if cont != 'y':
            break


def find_book(books_dict, book_id):
    if book_id in books_dict:
        return books_dict[book_id]  # Return book if found
    else:
        return None  # koi book nahi mili 


def borrow_book(book_list):
    book_id = input("Enter book ID to borrow: ")
    book = find_book(book_list, book_id)
    if book:
        if book["Status"] == "available":
            book["Status"] = "borrowed"
            print("You have borrowed the book successfully!")
        else:
            print("Sorry, this book is already borrowed.")
    else:
        print("Book not found in the library.")


def return_book(book_list):
    book_id = input("Enter book ID to return: ")
    book = find_book(book_list, book_id)
    if book:
        if book["Status"] == "borrowed":
            book["Status"] = "available"
            print("Book returned successfully!")
        else:
            print("This book was not borrowed.")
    else:
        print("Book not found in the library.")


#dispalying all book function 
def display_all_books(books_dict):
    if not books_dict:
        print("no books in the library ")
    else:
        print("\n inventorry library ")
        for book_id,details in books_dict.items():
            status_text = "available" if details["Status"] == "available" else "borrowed"
            print(f"\n Book ID: {book_id}")
            print(f" Title: {details['Title']}")
            print(f" Author: {details['Author']}")
            print(f" Year: {details['Year']}")
            print(f" Status: {status_text}")
  
def available_books(books_dict):
    print("\nAvailable Books:")
    found = False
    for book_id, details in books_dict.items():
        if details["Status"] == "available":  # Only show available ones
            found = True
            print(f"- {details['Title']} by {details['Author']} ({details['Year']}) [ID: {book_id}]")
    if not found:
        print("No books available at the moment!")

# Main function with dictionary to store books
def main():
    # Initialize empty dictionary to store books
    books = {}
    
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show Available Books")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            display_all_books(books)
        elif choice == '3':
            borrow_book(books)
        elif choice == '4':
            return_book(books)
        elif choice == '5':
            available_books(books)
        elif choice == '6':
            print("\nThank you for using the Library Management System!")
            break
        else:
            print("\nInvalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()


    
    

