# Menu-Driven CRUD Operations on a List of Books

books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book added")

    elif ch == 2:
        print("Books:", books)

    elif ch == 3:
        old = input("Enter book name to update: ")
        if old in books:
            new = input("Enter new book name: ")
            books[books.index(old)] = new
            print("Book updated")
        else:
            print("Book not found")

    elif ch == 4:
        book = input("Enter book name to delete: ")
        if book in books:
            books.remove(book)
            print("Book deleted")
        else:
            print("Book not found")

    elif ch == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")