import sqlite3

conn=sqlite3.connect('contacts.sqlite')
db=sqlite3.connect('contacts.sqlite')
name=input('what name:')
update_sql="update contacts set email='update@update.com' where name={}".format(name)
update_cursor=db.cursor()
update_cursor.execute(update_sql)
print('{} rows updated'.format(update_cursor.row))
for name, phone, email in db.execute('SELECT * from contacts'):
    print(name)
    print(phone)
    print(email)
    print('-'*40)

db.close()
 
conn.close()
