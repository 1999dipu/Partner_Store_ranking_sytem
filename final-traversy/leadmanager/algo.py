import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

for row in cur.execute('SELECT lockers_onboard.name,lockers_onboard.lockerid,lockers_availability.lockerid,lockers_availability.non_del_days FROM lockers_onboard ,lockers_availability WHERE  lockers_onboard.lockerid =lockers_availability.lockerid;'):
    print(row)

# Be sure to close the connection
con.close()