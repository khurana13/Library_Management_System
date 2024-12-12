# Library_Management_System

1. User Roles and Login:
   - The system supports three user roles: **Student**, **Faculty**, and **Librarian**.
   - Each role is prompted to enter a choice (`s`, `f`, or `l`) and authenticate with a username and password stored in predefined dictionaries (`student`, `faculty`, `librarian`).

2. Functionalities:
   - **Students and Faculty**:
     - View books issued to them.
     - View books available in the library.
   - **Librarians**:
     - Register new students and faculty with a 4-digit password.
     - Issue books to students or faculty if available in the library.
     - Accept book returns from students or faculty and update the inventory.
     - Add new books to the library's collection.

3. Data Storage:
   - Users and their passwords are stored in dictionaries (`student`, `faculty`, `librarian`).
   - Issued books are tracked separately for students and faculty using `books_issued_s` and `books_issued_f`.
   - Available books are stored in the `books_available` list.

4. Interaction:
   - Users are prompted for inputs based on their role and the functionality they choose.

The program ensures that:
- Only valid users with correct credentials can access the system.
- The librarian manages critical operations like registration, book issuing, and inventory updates.

