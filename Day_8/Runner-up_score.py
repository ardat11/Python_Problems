if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

mx= max(arr)

while arr.count(mx) > 0:
    arr.remove(max(arr))

print(max(arr))



