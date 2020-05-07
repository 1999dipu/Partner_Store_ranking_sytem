import sqlite3

def algoFun():
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
            locker_availability.status 
            from locker_onboard,locker_availability 
            where 
            locker_availability.lockerid_id = locker_onboard.lockerid;"""
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
                rank) values (?,?,?,?,?,?,?,?,?,?);"""
    rank=1
    lstRow=[]
    for row in cur.execute(qry):
        row+=(rank,)
        rank=rank+1
        lstRow.append(row)
        
    cur.executemany(qryInsrt,lstRow)

    for row in cur.execute('select * from locker_rankinglist;'):
        print(row)
    con.commit()
    con.close()