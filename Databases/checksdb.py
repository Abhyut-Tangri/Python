import sqlite3

db = sqlite3.connect('accounts.sqlite')

query = """
SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') as localtime,
       history.account,
       history.amount
FROM history
ORDER BY history.time
"""

for row in db.execute(query):
    print(row)

db.close()
