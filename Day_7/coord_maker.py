#Problem :https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

perm = []

for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            perm.append([a, b, c])

filtered_perm = [group for group in perm if sum(group) != n]

print(filtered_perm)
