import pandas as pd
import matplotlib.pyplot as plt

def IP_Bar():
    df = pd.read_csv("C:\\project\\library.csv")
    genre_count = df['Genre'].value_counts()
    plt.bar(genre_count.index, genre_count.values)
    plt.xlabel('Genre')
    plt.ylabel('Number of Books')
    plt.title('Books per Genre')
    plt.show()

def search():
    df = pd.read_csv("C:\\project\\library.csv")
    df.set_index('Book ID', inplace=True)
    book_id = int(input("Enter the existing Book ID to be displayed: "))
    print(df.loc[[book_id]])

def modify_book():
    df = pd.read_csv("C:\\project\\library.csv")
    df.set_index('Book ID', inplace=True)
    book_id = int(input("Enter the existing Book ID: "))
    field = input("Enter the field to modify (Title, Author, Genre, or Year): ").capitalize()
    new_value = input(f"Enter the new value for {field}: ")
    df.at[book_id, field] = new_value
    df.reset_index(inplace=True)
    df.to_csv("C:\\project\\library.csv", index=False)

def delete_book():
    df = pd.read_csv("C:\\project\\library.csv")
    df.set_index('Book ID', inplace=True)
    book_id = int(input("Enter the Book ID of the book to be deleted: "))
    df = df.drop(book_id)
    df.reset_index(inplace=True)
    df.to_csv("C:\\project\\library.csv", index=False)

def add_book():
    df = pd.read_csv("C:\\project\\library.csv")
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre = input("Enter Genre: ")
    year = int(input("Enter Year of Publication: "))
    df = df.append({'Book ID': book_id, 'Title': title, 'Author': author, 'Genre': genre, 'Year': year}, ignore_index=True)
    df.to_csv("C:\\project\\library.csv", index=False)

def menu():
    print("======================================")
    print("1. Show All Books")
    print("2. Add New Book")
    print("3. Delete a Book")
    print("4. Modify Book Details")
    print("5. Search for a Book")
    print("6. Show Bar Graph for Genres")
    print("0. Exit")
    print("======================================")
    
def show_books():
    df = pd.read_csv("C:\\project\\library.csv")
    print("======================================")
    print(df)
    print("======================================")
    input("Press Enter to continue...")

while True:
    menu()
    ans = int(input("Enter your choice: "))
    if ans == 0:
        print("\nGoodbye!")
        break
    elif ans == 1:
        show_books()
    elif ans == 2:
        add_book()
    elif ans == 3:
        delete_book()
    elif ans == 4:
        modify_book()
    elif ans == 5:
        search()
    elif ans == 6:
        IP_Bar()
