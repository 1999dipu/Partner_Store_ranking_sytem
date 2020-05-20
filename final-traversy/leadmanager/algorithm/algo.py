from algorithm import getRows
from algorithm import getSpecs
from algorithm import updRankingList

def algoFun(qry):
    x=qry["lattitude"]
    y=qry["longitude"]
    lockers=getRows.getrows(x,y)
    specLocker=[]
    for row in lockers:
        x=()
        x+=(row[0],)
        x=getSpecs.specs(row[0])
        x+=(row[9],)
        specLocker.append(x)
    print(specLocker)
    for y in specLocker:
        y+=("Naina",)
    updRankingList.updateR(lockers)