import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

#for row in cur.execute('SELECT lockers_onboard.name,lockers_onboard.lockerid,lockers_avilability.lockerid,lockers_avilability.non_del_days FROM lockers_onboard ,lockers_avilability WHERE  lockers_onboard.lockerid =lockers_avilability.lockerid;'):
for row in cur.execute('SELECT * from lockers_onboard;'):
    print(row)

# Be sure to close the connection
con.close()