import sqlite3

# 1. Connect and initialize database
conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
);

INSERT INTO books VALUES
(1, 'Data Science Basics', 'Tech', 1450, 10),
(2, 'Clean Code', 'Tech', 1200, 4),
(3, 'The Silent Patient', 'Fiction', 1350, 2),
(4, 'Python 101', 'Tech', 950, 15),
(5, 'Dune', 'Fiction', 1100, 8),
(6, 'To Kill a Mockingbird', 'Fiction', 800, 1),
(7, 'The Hobbit', 'Fantasy', 1250, 6),
(8, '1984', 'Fiction', 900, 3);
""")
conn.commit()

# Query (a) & (b): Price > 1000 sorted descending with AS aliasing
print("Books above Rs. 1000 (sorted):")
cur.execute("""
    SELECT title AS book_title, price 
    FROM books 
    WHERE price > 1000 
    ORDER BY price DESC;
""")
for row in cur.fetchall():
    print(row)

# Query (c): Fiction books with stock < 5
print("\nLow-stock Fiction books:")
cur.execute("""
    SELECT title, genre, price, stock 
    FROM books 
    WHERE genre = 'Fiction' AND stock < 5;
""")
for row in cur.fetchall():
    print(row)

conn.close()