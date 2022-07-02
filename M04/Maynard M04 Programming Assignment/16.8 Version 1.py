import sqlite3

conn = sqlite3.connect('books.db')

c = conn.cursor()

c.execute("""CREATE TABLE books (
            title text,
            author text,
            year integer
            )""")

ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'
c.execute(ins, ('The Weirdstone of Brisingamen','Alan Garner',1960))
c.execute(ins, ('Perdido Street Station', 'China Miéville',2000))
c.execute(ins, ('Thud!', 'Terry Pratchett',2005))
c.execute(ins, ('The Spellman Files', 'Lisa Lutz',2007))
c.execute(ins, ('Small Gods', 'Terry Pratchett',1992))

c.execute('SELECT * FROM books')

rows = c.fetchall()
print(rows)

conn.commit()
c.close()
conn.close()