import sqlite3
def createLocker(infoLocker):
    """{'address': 'Delhi', 
    'zipcode': '201001', 
    'lockername': 'ABCD', 
    'num_of_locker': '12', 
    'daystring': '1110000', 
    'start_time': '07:00', 
    'end_time': '22:00', 
    'lattitude': 28.6517178, 
    'longitude': 77.2219388}"""
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    pk=0
    for row in cur.execute('SELECT lockerid from locker_onboard'):
        if pk<row[0]:
            pk=row[0]
    pk = pk+1
    row=()
    row+=(pk,)
    row+=(infoLocker["lockername"],)
    row+=("India",)
    row+=(infoLocker["address"],)
    row+=(infoLocker["zipcode"],)
    row+=(int(infoLocker["num_of_locker"]),)
    row+=(infoLocker["lattitude"],)
    row+=(infoLocker["longitude"],)
    qryInsrt = """insert into locker_onboard
                (lockerid,
                name,
                country	,
                address,
                zipcode,
                total_slots,
                latitude,
                longitude) values (?,?,?,?,?,?,?,?)"""
    l=[]
    l.append(row)
    print(l)
    cur.executemany(qryInsrt,l)
    con.commit()
    con.close()

