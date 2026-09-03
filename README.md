# Library-Checkout-System
*Mini-project to learn OOP*

**Project Goals & Constraints (original)**
Build a small command-line (or just script-run) system that models a library. No UI needed — just the classes and a main that exercises them.

*Requirements:*
There are Books. Each has a title, author, and an ISBN.
There are Members who can borrow books. Each has a name and a member ID.

A Library holds a collection of books and members, and handles:
- Checking a book out to a member
- Returning a book
- Listing which books are currently checked out, and to whom
- Preventing a book being checked out if it's already out

*Adding twists:*
Add a second type of item — DVD, which also has a title but instead of an author has a runtime, and has a different max loan period than a book (books: 21 days, DVDs: 7 days). Both need to be checkout-able through the same Library interface.

*Things to consider:*
Should Book and DVD share a parent class? What would that parent actually contain — and what should NOT go in it?
Where does "max loan period" live — on the item itself, or somewhere else? Why?
Should Library know the difference between a Book and a DVD when checking something out, or should it not care?
What should be private inside each class vs. accessible from outside?