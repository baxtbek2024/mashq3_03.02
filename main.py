
#1-masala

dict1 = {'a': 10, 'b': 20, 'c': 5}
dict2 = {'b': 5, 'c': 15, 'd': 7}
result = dict1.copy()

for i, x in dict2.items():
    if i in result:
        result[i] += x
    else:
        result[i] = x
print(result)

#2-masala

dict1 = {"a": 20, "b": 11, "c": 20}

toza = {}

for k, v in dict1.items():
    toza[v] = k

print(toza)

#3-masala

text = "salom dostim nima gap, salom senga"

sozlar = text.split()
kop_uchraydigan = {}

for i in sozlar:
    if i in kop_uchraydigan:
        kop_uchraydigan[i] += 1
    else:
        kop_uchraydigan[i] = 1

top3 = sorted(kop_uchraydigan, key=kop_uchraydigan.get, reverse=True)[:3]

print(kop_uchraydigan)
print(top3)

#4-masala

d = {'a': 10, 'b': 25, 'c': 5, 'd': 30}
limit = 15

result = {}

for k, v in d.items():
    if v > limit:
        result[k] = v

print(result)

