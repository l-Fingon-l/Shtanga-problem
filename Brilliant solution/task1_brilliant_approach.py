################################################
## The following piece of code was written by
##          Arseniy Parfenov, 2022
################################################


r  = 1
g  = 12.0
xs = [4.5]*2 + [8.5]*2 + [13.0]*2 + [11.0]*4 # Диски
ws = {0.0 : {g}}
 
for x in xs:
    wsn = {}
    for d,s in ws.items():
        wsn[d] = wsn.get(d,set()) | s
        sp = {x+y for y in s}
        for dp in (round(abs(d+x),r), round(abs(d-x),r)):
            wsn[dp] = wsn.get(dp,set()) | sp
    ws = wsn
 
print(*sorted(ws[0]), sep=', ')