lst = list(map(int, input().split()))
prize = 0
for i in lst:
    if lst.count(i) == 3:
        prize = 10000 + i * 1000
    elif lst.count(i) == 2:
        prize = 1000 + i * 100
    else:
        if prize < i * 100:
            prize = i * 100
print(prize)