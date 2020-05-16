import sqlite3
import math

def algoFun(qry):

    """
    key: addressfield Value: 166, MUKUND NAGAR GHAZIABAD
    key: zipfield Value: 201001
    key: landmarksfield Value: 
    key: lockerfield Value: 
    key: query Value: storeZip
    key: lattitude Value: 28.674865
    key: longitude Value: 77.4318992
    """
    zipcode=qry["zipfield"]
    x=qry["lattitude"]
    y=qry["longitude"]
    print(x,y)
    print()
    print()
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute('delete from locker_rankinglist')
    qry="""select locker_availability.lockerid_id,
            locker_onboard.name,
            locker_onboard.country,
            locker_onboard.address,
            locker_onboard.zipcode,
            locker_availability.non_del_days,
            locker_availability.timings_open,
            locker_availability.timings_closed,
            locker_availability.status,
            locker_coordinates.latitude,
            locker_coordinates.longitude 
            from locker_onboard,locker_availability,locker_coordinates
            where 
            locker_availability.lockerid_id = locker_onboard.lockerid
            and locker_onboard.lockerid = locker_coordinates.lockerid_id
            and locker_onboard.zipcode = """ + zipcode+";"
    qryInsrt = """insert into locker_rankinglist 
                (lockerid_id,
                name,
                country,
                address,
                zipcode,
                non_del_days,
                timings_open,
                timings_closed,
                status,
                rank,
                dist) values (?,?,?,?,?,?,?,?,?,?,?);"""
    rank=1
    lstRow=[]
    for row in cur.execute(qry):
        dist=(row[9]-x)*(row[9]-x)+(row[10]-y)*(row[10]-y)
        row=row[:9]
        row+=(rank,)
        rank=rank+1
        dist=math.sqrt(dist)
        row+=(dist,)
        lstRow.append(row)
        
    cur.executemany(qryInsrt,lstRow)

    print("RANKING LIST UPDATED")
    con.commit()
    con.close()