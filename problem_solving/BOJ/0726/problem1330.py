a, b = map(int, input().split())
if a > b:
    print('>') #A가 B보다 큰 경우에는 '>'를 출력한다.
elif a < b:
    print('<') #A가 B보다 작은 경우에는 '<'를 출력한다.
elif a == b:
    print('==') #A와 B가 같은 경우에는 '=='를 출력한다.