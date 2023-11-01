x = input()

unique = []

for harf in x:
    if x.count(harf) < 2:
        unique.append(harf)


print(unique)