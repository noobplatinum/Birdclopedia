
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    ALTER TABLE users ADD COLUMN bio TEXT DEFAULT '';
''')
cursor.execute('''
    ALTER TABLE users ADD COLUMN favorites TEXT DEFAULT '';
''')

conn.commit()
conn.close()
print("Database updated successfully!")
