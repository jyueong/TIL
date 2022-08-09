right = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))
howmany = ''
for idx, value in enumerate(white):
    howmany += str(right[idx] - value)
    howmany += ' '

print(howmany)