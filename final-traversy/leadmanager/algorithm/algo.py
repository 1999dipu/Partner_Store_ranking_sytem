from algorithm import getRows
from algorithm import updRankingList

def algoFun(qry):
    x=qry["lattitude"]
    y=qry["longitude"]
    rows=getRows.getrows(x,y)
    updRankingList.updateR(rows)