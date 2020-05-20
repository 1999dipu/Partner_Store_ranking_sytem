import sqlite3
import math
#returns list of row in the following format:
"""lockerid_id,name,country,address,zipcode,non_del_days,
    timings_open,timings_closed,status,latitude,longitude,
    dist,dummyRank"""

def getrows(x,y):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    qry="""select locker_availability.lockerid_id,
            locker_onboard.name,
            locker_onboard.country,
            locker_onboard.address,
            locker_onboard.zipcode,
            locker_availability.non_del_days,
            locker_availability.timings_open,
            locker_availability.timings_closed,
            locker_availability.status,
            locker_onboard.latitude,
            locker_onboard.longitude 
            from locker_onboard,locker_availability
            where 
            locker_availability.lockerid_id = locker_onboard.lockerid"""
    
    lstRow=[]
    dummyRank=0
    for row in cur.execute(qry):
        dist=(row[9]-x)*(row[9]-x)+(row[10]-y)*(row[10]-y)
        row=row[:9]
        dist=math.sqrt(dist)
        row+=(dist,)
        row+=(dummyRank,)
        lstRow.append(row)
    
    con.close()
    print("ROW FETCHED") 
    return lstRow