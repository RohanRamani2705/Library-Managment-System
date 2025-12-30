Library Management System

Overview

The Library Management System is a simple yet effective Python-based application designed to manage a collection of books stored in a CSV file. It provides an interactive, menu-driven interface that allows users to efficiently perform common library operations such as adding, deleting, modifying, searching, and visualizing books.

The system leverages pandas for data manipulation and matplotlib for visualizing book distribution by genre, making it both practical and educational for beginners and intermediate Python users.

Features:

Add new books to the library
Delete existing books by Book ID
Modify book details (title, author, genre, year)
Search for a book using a unique Book ID
Display all books in a tabular format
Visualize book distribution by genre using a bar chart
Persistent storage using a CSV file (library.csv)


Technologies Used

Python 3.x
Pandas – Data handling and CSV manipulation
Matplotlib – Data visualization (bar charts)


Prerequisites

Ensure the following are installed before running the system:

pip install pandas matplotlib

You will also need a CSV file named library.csv with the following structure:

CSV File Format

Book ID,Title,Author,Genre,Year
1,The Great Gatsby,F. Scott Fitzgerald,Fiction,1925
2,1984,George Orwell,Dystopian,1949
3,To Kill a Mockingbird,Harper Lee,Fiction,1960
4,The Catcher in the Rye,J.D. Salinger,Fiction,1951
5,The Hobbit,J.R.R. Tolkien,Fantasy,1937


How the System Works

Show All Books:
Displays all books stored in library.csv in a clean tabular format.

Process
Loads the CSV file using pandas
Prints all records to the console
Waits for user input before returning to the menu

Add New Book:
Adds a new book by collecting user input.

Process
Prompts for Book ID, Title, Author, Genre, and Year
Appends the new record to the CSV file

Delete a Book:
Removes a book using its unique Book ID.

Process
User enters the Book ID
The matching record is removed from the CSV file

Modify Book Details:
Allows modification of any field of an existing book.

Process
User selects the Book ID
Chooses which field to update (Title, Author, Genre, or Year)
Updates the CSV file accordingly

Search for a Book:
Searches for a book using its Book ID.

Process
Uses pandas indexing to locate the book
Displays the book details if found

Show Genre Distribution (Bar Chart):
Visualizes the number of books in each genre.

Process
Counts genres using value_counts()
Displays a bar chart using matplotlib


How to Run the Program

Clone or Download the Repository
Ensure library.csv exists in the correct directory (Example path: C:\project\library.csv)


Run the program:

python library_management_system.py

🖥️ Example Menu Interaction
1. Show All Books
2. Add New Book
3. Delete a Book
4. Modify Book Details
5. Search for a Book
6. Show Bar Graph for Genres
0. Exit
======================================
Enter your choice: 1


Output:

Book ID | Title                  | Author              | Genre     | Year
1       | The Great Gatsby       | F. Scott Fitzgerald | Fiction   | 1925
2       | 1984                   | George Orwell       | Dystopian | 1949
...


Conclusion:

The Library Management System provides a simple, intuitive, and effective solution for managing a collection of books. It is ideal for learning data handling with pandas, file-based persistence using CSVs, and basic data visualization.

The project is highly extensible—new features such as user authentication, database integration, or advanced analytics can easily be added.

Contributions:

Contributions, improvements, and suggestions are welcome.
Feel free to fork the project and enhance its capabilities.
