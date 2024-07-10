import sqlite3


db=sqlite3.connect('contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts(name text, phone integer, email text)')
db.execute("INSERT INTO contacts(name,phone, email) VALUES('tim',6564678,'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian',1234,'brian@myemail.com')")
db.execute("INSERT INTO contacts VALUES('Steve',87654,'steve@hisemail.com')")
db.execute("INSERT INTO contacts VALUES('avril','61(0)2178327892','avril@gmail.com')")

cursor=db.cursor()
cursor.execute("SELECT * FROM contacts")

#print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name,phone,email in cursor:
    print(name)
    print(phone)
    print(email)
    print('-'*40)

cursor.close()
db.commit()
db.close()
