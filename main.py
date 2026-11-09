from models import LibraryItem, Book, Magazine, DVD, Member


def main():
    book = Book("Python 101", 1, "A. Rao")
    magazine = Magazine("Science Today", 2, 12)
    dvd = DVD("Planet Earth", 3, 60)

    alice = Member("Alice", 101)
    bob = Member("Bob", 102, max_items=1)

    print("CAMPUS LIBRARY MANAGER")
    print("\nBorrowing items")
    try:
        alice.borrow(book)
        print("Alice borrowed:", book.describe())
    except ValueError as e:
        print("Could not borrow:", e)

    # Neither Alice nor Bob can borrow the book while Alice has it.
    for member in [alice, bob]:
        try:
            member.borrow(book)
        except ValueError as e:
            print("Could not borrow:", e)

    try:
        bob.borrow(magazine)
        print("Bob borrowed:", magazine.describe())
        bob.borrow(dvd)
    except ValueError as e:
        print("Could not borrow:", e)

    try:
        alice.borrow(dvd)
        print("Alice borrowed:", dvd.describe())
    except ValueError as e:
        print("Could not borrow:", e)

    print("Alice's borrowed titles:", alice.borrowed_titles())
    print("Bob's borrowed titles:", bob.borrowed_titles())

    print("\nLate fees")
    items = [book, magazine, dvd]
    for item in items:
        print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

    print("\nReturning items")
    try:
        alice.return_item(magazine)
    except ValueError as e:
        print("Could not return:", e)

    try:
        fee = alice.return_item(book, days_late=3)
        print("Alice returned Python 101. Late fee: Rs", fee)
        fee = alice.return_item(dvd)
        print("Alice returned Planet Earth on time. Late fee: Rs", fee)
        fee = bob.return_item(magazine, days_late=3)
        print("Bob returned Science Today. Late fee: Rs", fee)
    except ValueError as e:
        print("Could not return:", e)

    print("Alice's borrowed titles after returns:", alice.borrowed_titles())
    print("Bob's borrowed titles after returns:", bob.borrowed_titles())

    print("\nEncapsulation")
    try:
        print(book.__available)
    except AttributeError:
        print("AttributeError: __available cannot be read directly.")
    print("Book available using is_available():", book.is_available())

    print("\nAbstract class")
    try:
        LibraryItem("Test item", 4)
    except TypeError:
        print("TypeError: LibraryItem cannot be created because late_fee() is abstract.")

    print("\nTotal items created:", LibraryItem.total_items)


if __name__ == "__main__":
    main()
