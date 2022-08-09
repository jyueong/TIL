while True:
    n = int(input())  # 단어 개수 입력받기
    if n == 0:  # n이 0이면 종료
        break
    words = []  # 단어들이 들어갈 리스트 생성
    for i in range(n):  # 단어 개수 만큼 입력받기
        word = input()
        words.append([word.lower(), word])
        # 대소문자 관계없이 정렬하기 위해 word.lower()
        # 최종적으로 입력받은 형태 그대로 출력하기 위해 word
        # 두 가지 요소를 다 리스트에 넣어주기
    words = sorted(words)  # 정렬
    print(words[0][1])  # 가장 앞에 오는 리스트의 두번째 값(입력받은 형태)을 출력