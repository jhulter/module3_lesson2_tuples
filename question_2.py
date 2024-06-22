# Task 1
author = ""
title = ""


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    try:
        title = input("Enter the book you wish to add to the library: ")
        author = input("Enter the author of that book: ")
        book = (title, author)

        if book not in library:
            library.append(book)
            print(f"{book} has been added to the library!")
        else:
            print(f"Library already contains {book}")
    except ValueError:
        print("Invalid entry...")

add_book(library)

def show_library(library):
    for a, b in library:
        print(f"Your library contains: {a} by {b}")

show_library(library)
