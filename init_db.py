import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Example Post', 'Content for the first post blah blah blah')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Example Post', 'Content for the second post blah blah blah')
            )

connection.commit()
connection.close()