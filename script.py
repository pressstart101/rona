import sqlite3


#1. Connect to database
# 2. Create cursor object (cursor objet is a pointer to access rows from the table of the database)
# 3. Apply sql query(insert data in the database)
# 4. Commit changes to db
# 5. Close the connection
def create_table():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS daily_deaths (country INTEGER, state INTEGER, city INTEGER)")
    conn.commit()
    conn.close()

def insert(country, state, city):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO daily_deaths VALUES (?,?,?)",(country, state, city))
    conn.commit()
    conn.close()

# insert()

def view_all():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('SELECT rowid, * FROM daily_deaths')
    rows=cur.fetchall()
    conn.close()
    return rows

def view_one(one):
    conn=sqlite3.connect('lite.db')
    conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute('SELECT rowid, * FROM daily_deaths') 
    row = cur.fetchone()
    # names = row.keys()
    rows=cur.fetchall()
    for row in rows:
        print(row[one])
    conn.close()
    return row[one]
    # return rows



# print(view_all())
# print(view_one("country"))