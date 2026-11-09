# Campus Library Manager

A Python program for borrowing and returning books, magazines and DVDs. Each item type has a different late fee, and invalid borrow or return attempts show an error message.

## How to run

Use Python 3.12 or later. Open a terminal in the folder containing the files and run:

```bash
python3 main.py
```

No extra packages are needed. The demo output is saved in `output.txt`.

## Questions

### 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

`LibraryItem` contains the common details and methods for all three item types. It makes `late_fee()` abstract so each item type must provide its own fee calculation. If `DVD` does not implement this method, trying to create a DVD object raises a `TypeError`.

### 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Reading `item.__available` directly raises an `AttributeError` because Python changes the internal name of double-underscore attributes through name mangling. We use `is_available()` to check availability through a method instead of accessing the internal attribute. This helps avoid accidental changes, although name mangling does not completely prevent access.

### 3. What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is a shared class attribute that counts the item objects created across books, magazines and DVDs. `self.title` is an instance attribute, so each item has its own title.
