# TODO

## main.py
1. Add book
2. Search book (LIKE) and show if issued
    - maybe add category dropdown menu
3. Issue book
4. Return Book
5. Show issued books*

## db.py
1. new connection
2. add data if not exists & create current table
3. search book to show (issued=True for (5*))
4. search book to enter into fields
4. issue book - add to current table
5. return book - remove from current table

## database

### books
book_id, book, author, type, issued

### current
book_id, student_id

### students
student_id, name, class