################################################
## The following piece of code was written by
##          Amina Miphtahova, 2022
################################################


from itertools import combinations
from collections import Counter

def is_sublist(l, original_cnt):
    # функция чтоб проверять, содержится ли один список полностью внутри другого
    l_cnt = Counter(l)
    for k, v in l_cnt.items():
        if k not in original_cnt:
            return False
        elif v > original_cnt[k]:
            return False
    return True

weights = [4.5, 4.5, 8.5, 8.5, 13, 13, 11, 11, 11, 11]
g = 12

# перебираем все возможные варианты комбинаций блинов
combs = []
for i in range(1, len(weights)):
    combs += [list(x) for x in combinations(weights, i)]

# проходимся по всем парам комбинаций и смотрим, чтобы
# а) сумма блинов в первом элементе пары была равна сумме во втором элементе пары
# б) если объединить списки внутри пары, то все веса содержатся внутри оригинального списка весов
original_cnt = Counter(weights)
results = set()
results.add(g)
for i in range(len(combs)):
    for j in range(i + 1, len(combs)):
        if sum(combs[i]) == sum(combs[j]):
            if is_sublist(combs[i] + combs[j], original_cnt):
                results.add(sum(combs[i]) * 2 + g)

print(sorted(list(results)))
