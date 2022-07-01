"""
reads the given database and prints every line.
"""
import sqlalchemy as sa

# table called books with these fields: title (text), author (text), and year (integer).
# conn = sqlite3.connect('books.db')

path = 'books2.db'
conn = sa.create_engine(f'sqlite:///{path}')

# conn.execute("""CREATE TABLE books (
#             title text,
#             author text,
#             year integer
#             )""")

# ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'
# conn.execute(ins, ('The Weirdstone of Brisingamen','Alan Garner',1960))
# conn.execute(ins, ('Perdido Street Station', 'China Miéville',2000))
# conn.execute(ins, ('Thud!', 'Terry Pratchett',2005))
# conn.execute(ins, ('The Spellman Files', 'Lisa Lutz',2007))
# conn.execute(ins, ('Small Gods', 'Terry Pratchett',1992))


rows = conn.execute('SELECT * FROM books')
for row in rows:
    print(row)
