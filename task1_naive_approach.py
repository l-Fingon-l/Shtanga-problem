import time

#  Uslovie
grif = 12
bliny = [4.5, 4.5, 8.5, 8.5, 11, 11, 11, 11, 13, 13]
coefficienty = [1] * len(bliny)
varianty = {}

#  Ves perekosa na odnu storonu shtangi
def perekos():
    suma_blinov = 0
    for i in range(len(bliny)):
        suma_blinov += coefficienty[i] * bliny[i]
    return suma_blinov


# Ves shtangi s odetim naborom blinov
def ves():
    suma_blinov = 0
    for i in range(len(bliny)):
        suma_blinov += abs(coefficienty[i]) * bliny[i]
    return suma_blinov + grif


# Nabor blinov dlya vesa vishe
def nabor_blinov():
    nabor = [[], []]
    for i in range(len(bliny)):
        if coefficienty[i] == 1:
            nabor[0].append(bliny[i])
        elif coefficienty[i] == -1:
            nabor[1].append(bliny[i])
    return nabor


def vzvesit(index=-1, coefficient=1):
    if index < len(bliny):
        coefficienty[index] = coefficient
        vzvesit(index + 1, 1)
        vzvesit(index + 1, 0)
        vzvesit(index + 1, -1)
    else:
        if perekos() == 0:
            varianty[ves()] = nabor_blinov()

#  Samo rezhenie!
start = time.time()
vzvesit()
print(len(varianty))
for [ves, nabor_blinov] in sorted(varianty.items()):
    print(str(ves) + ':\t' + str(nabor_blinov[0]) + ' <===> ' + str(nabor_blinov[1]))
end = time.time()
# print('\nAmount of blinov: ' + str(len(bliny)))
print('Time spent: ' + str(end - start))
