print("Welcome to Library Management System")
print("press s if you are a student")
print("press f if you are a faculty")
print("press l if you are a librarian")

# Initial dictionaries
student = {"Sneha": 7418}
faculty = {"DrSmith": 1234}
librarian = {"ABC": 123}
books_issued_s = {}
books_issued_f = {}
books_available = ["Book1", "Book2", "Book3"]

while True:
    ch = input("Enter your choice (s/f/l or 'exit' to quit): ")

    if ch.lower() == "s":  # Student Section
        name = input("Enter your name: ")
        if name in student:
            print("Valid user")
            d = int(input("Enter Password: "))
            if d == student[name]:
                print("Correct Password")
                print("1 for viewing books issued")
                print("2 for viewing books available")
                h = int(input("Enter your choice: "))
                if h == 1:
                    if name not in books_issued_s or not books_issued_s[name]:
                        print("No books issued")
                    else:
                        print("The books issued are:", books_issued_s[name])
                elif h == 2:
                    print("Books available:", books_available)
                else:
                    print("Invalid choice")
            else:
                print("Incorrect Password")
        else:
            print("Invalid user")

    elif ch.lower() == "f":  # Faculty Section
        name = input("Enter your name: ")
        if name in faculty:
            print("Valid user")
            d = int(input("Enter Password: "))
            if d == faculty[name]:
                print("Correct Password")
                print("1 for viewing books issued")
                print("2 for viewing books available")
                h = int(input("Enter your choice: "))
                if h == 1:
                    if name not in books_issued_f or not books_issued_f[name]:
                        print("No books issued")
                    else:
                        print("The books issued are:", books_issued_f[name])
                elif h == 2:
                    print("Books available:", books_available)
                else:
                    print("Invalid choice")
            else:
                print("Incorrect Password")
        else:
            print("Invalid user")

    elif ch.lower() == "l":  # Librarian Section
        name = input("Enter your name: ")
        if name in librarian:
            print("Valid user")
            d = int(input("Enter Password: "))
            if d == librarian[name]:
                print("Correct Password")
                print("1 for registering a student")
                print("2 for registering a faculty")
                print("3 for issuing a book for a student")
                print("4 for issuing a book for faculty")
                print("5 for returning a book for a student")
                print("6 for returning a book for faculty")
                print("7 for adding a book to the library")
                h = int(input("Enter your choice: "))
                if h == 1:  # Registering a Student
                    a = input("Enter name of student: ")
                    b = int(input("Enter a 4-digit password: "))
                    student[a] = b
                    print("Student Registered Successfully!")
                elif h == 2:  # Registering a Faculty
                    a = input("Enter name of faculty: ")
                    b = int(input("Enter a 4-digit password: "))
                    faculty[a] = b
                    print("Faculty Registered Successfully!")
                elif h == 3:  # Issuing a Book for Student
                    name = input("Enter name of student: ")
                    if name in student:
                        book = input("Book to be issued: ")
                        if book in books_available:
                            books_available.remove(book)
                            books_issued_s.setdefault(name, []).append(book)
                            print("Book successfully issued to student!")
                        else:
                            print("Sorry, book not available")
                    else:
                        print("Student not registered")
                elif h == 4:  # Issuing a Book for Faculty
                    name = input("Enter name of faculty: ")
                    if name in faculty:
                        book = input("Book to be issued: ")
                        if book in books_available:
                            books_available.remove(book)
                            books_issued_f.setdefault(name, []).append(book)
                            print("Book successfully issued to faculty!")
                        else:
                            print("Sorry, book not available")
                    else:
                        print("Faculty not registered")
                elif h == 5:  # Returning a Book for Student
                    name = input("Enter name of student: ")
                    if name in books_issued_s and books_issued_s[name]:
                        book = input("Book to be returned: ")
                        if book in books_issued_s[name]:
                            books_issued_s[name].remove(book)
                            books_available.append(book)
                            print("Book successfully returned by student!")
                        else:
                            print("Book not issued to the student")
                    else:
                        print("No books issued to this student")
                elif h == 6:  # Returning a Book for Faculty
                    name = input("Enter name of faculty: ")
                    if name in books_issued_f and books_issued_f[name]:
                        book = input("Book to be returned: ")
                        if book in books_issued_f[name]:
                            books_issued_f[name].remove(book)
                            books_available.append(book)
                            print("Book successfully returned by faculty!")
                        else:
                            print("Book not issued to the faculty")
                    else:
                        print("No books issued to this faculty")
                elif h == 7:  # Adding a Book to the Library
                    book = input("Enter name of the book: ")
                    books_available.append(book)
                    print("Book added successfully!")
                else:
                    print("Invalid choice")
            else:
                print("Incorrect Password")
        else:
            print("Invalid user")

    elif ch.lower() == "exit":  # Exit Condition
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid input. Please try again.")
