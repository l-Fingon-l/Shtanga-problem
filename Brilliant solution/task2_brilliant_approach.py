################################################
## The following piece of code was written by
##          Arseniy Parfenov, 2022
################################################


r = 1
g = 12.0
xs = [4.5] * 2 + [8.5] * 2 + [11.0] * 4 + [13.0] * 2  # Диски

for x in xs:
    wsn = {}
    for d, s in ws.items():
        wsn[d] = wsn.get(d, set()) | s
        sp = {x + y for y in s}
        for dp in (round(abs(d + x), r), round(abs(d - x), r)):
            wsn[dp] = wsn.get(dp, set()) | sp
    ws = wsn

print("num of ws:", len(ws[0]))
print(sorted([int(w) for w in ws[0]]))

dws = sorted(ws.keys())[1:]
wnums = {}

for w1 in dws:
    for w2 in dws:
        if w1 <= w2:
            s = ws[0] | {round(w + w1, r) for w in ws[w1]} | {round(w + w2, r) for w in ws[w2]}
            s = s | {round(w + w1 + w2, r) for w in ws.get(round(w1 + w2, r), set())}
            s = s | {round(w + w1 + w2, r) for w in ws.get(round(w2 - w1, r), set())}
            wnums[(w1, w2)] = len(s)

max_inc = max(wnums.values())
print()
print(f"best incs ({max_inc}): ", [k for k, v in wnums.items() if v == max_inc])
