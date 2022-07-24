# IDE 기능

- 세로 커서: `Alt + Ctrl + 화살표`

- 특정 단어 바꾸기: `Ctrl + D`

- 줄 바꿈: `Alt + 화살표`

- 줄 복사: `Alt + shift + 화살표`

# 코드 작성법

- PEP8

- 주석: 코드에 대한 설명
  
  - 한 줄 주석: 주석으로 처리될 내용 앞에 `#`을 입력
  
  - 여러 줄 주석: 한 줄씩 '#'을 사용하거나 `"""` 또는 `'''` 으로 묶어서 표현

# 변수

- why? 추상화(복잡한 값들을 쉽게 사용하기 위해)

- `=`를 통해 값을 할당

- 이름
  
  - 영문 알파벳, 언더바, 숫자로 구성
  
  - 첫 글자에 숫자가 올 수 없음
  
  - 대소문자 구별
  
  - 예약어는 변수 이름으로 사용불가
  
  - 내장 함수, 모듈 등의 이름은 사용하지 않아야 함

# 자료형 분류

- 수치형
  
  - 정수 자료형(int)
  
  - 실수 자료형(float)
    
    - 부동 소수점 주의 >> 매우 작은 수보다 작은지를 확인 or math 모듈 활용

- 문자열
  
  - str 타입
  
  - `''` or `""` 활용하여 표기 >> 소스코드 내에서 하나의 문장부호를 선택하여 유지
  
  - Escape sequence `\`
  
  - Striping Interpolation: 문자열을 변수를 활용하여 만드는 법
    
    - f-strings 활용
    
    - ```python
      name = 'Kim'
      score = '4.5'
      
      print(f'Hello, {name}! 성적은 {score}')
      # Hello, Kim! 성적은 4.5
      ```

- 불린형
  
  - 논리 자료형
  
  - `True / False`를 값으로 가짐
  
  - 비교 / 논리 연산에서 활용
  
  - 논리 연산자
    
    - Falsy: False는 아니지만 False로 취급되는 다양한 값
      
      - `0, 0.0, (), [], {}, None, ""(빈 문자열)`
      
      - 우선순위: not, and, or 순으로 우선순위가 높음

- None
  
  - 값이 없음을 표현하기 위함
  
  - 반환 값이 없는 함수에서 사용하기도 함

# 컨테이너

- 여러 개의 값을 담을 수 있는 것

- 서로 다른 자료형 저장 가능

- 순서가 있는 데이터(시퀀스형)
  
  - 순서가 있다는 말이 정렬되어 있다는 말은 아님
  
  - 리스트, 튜플, 레인지

- 순서가 없는 데이터(비시퀀스형)
  
  - 세트, 딕셔너리

# 시퀀스형 컨테이너

## 리스트

- 생성
  
  - `[value1, value2, value3]`
  
  - `list()`

- 인덱스
  
  - `list[i]`
    
    - 0부터 시작
    
    - 뒤에서부터 셀 때는 -1부터 시작

## 튜플

- 생성
  
  - `(value1, value2)`
  
  - 값이 하나일 때는 `(value1,)` << 쉼표 필요

- 활용
  
  - `x, y = (1, 2)` >> 각각 할당됨
  
  - 빈 tuple 만들려면? ()

## 레인지

- 정수의 시퀀스를 나타내기 위함

- 기본형 : `range(n)`
  
  - 0부터 (n-1)까지

- 범위 지정 : `range(n, m)`
  
  - n부터 (m-1)까지

- 범위 및 스텝 지정 : `range(n, m, s)`
  
  - n부터 (m-1)까지 s만큼 증가한다
    
    - ex) list(range(1, 6, 2)) >> [1, 3, 5]

# 비시퀀스형 컨테이너

## 세트

- 중복되는 요소 X

- 인덱스를 이용한 접근 X

- 차집합(`-`), 합집합(`|`), 교집합(`&`), 대칭차집합: 교집합의 여집합(`^`)

- `{}`, `set()` 을 통해 생성

## 딕셔너리

- `key` + `value`

- `{key1: value1, key2: value2, key: value3}`

# 형변환

## 암시적 형변환

- 사용자 ㄴㄴ, 파이썬 내부적으로 자동으로 형변환 하는 경우

- `bool`
  
  - `True + 임의의 정수` >> True를 1로 계산

- `Numeric Type (int, float, complex)`
  
  - `int + float`, `int + complex`

## 명시적 형변환

|           | int   | float | str |
| --------- | ----- | ----- | --- |
| **int**   |       | O     | O   |
| **float** | O     |       | O   |
| **str**   | O(형식) | O(형식) |     |

## 컨테이너형 형변환

|        | string | list    | tuple   | range | set     | dict |
| ------ | ------ | ------- | ------- | ----- | ------- | ---- |
| string |        | O       | O       | X     | O       | X    |
| list   | O      |         | O       | X     | O       | X    |
| tuple  | O      | O       |         | X     | O       | X    |
| range  | O      | O       | O       |       | O       | X    |
| set    | O      | O       | O       | X     |         | X    |
| dict   | O      | O(key만) | O(key만) | X     | O(key만) |      |

# 기타

- 제곱근 구하기?
  
  - `a\**1/2`
  
  - ```python
    import math
    math.sqrt(a)
    ```

- scores 리스트의 평균?
  
  - ```python
    scores = [80, 70, 90, 100]
    s = 0
    cnt = 0
    for value in scores:
        s += value
        cnt += 1
    print(s / cnt)
    ```

- 문자열을 리스트로 변경하고 싶다면
  
  - ```python
    bts = '김남준 김석진 민윤기 정호석 박지민 김태형 전정국 비티에스'
    bts_list = bts.split()
    #공백을 기준으로 리스트 요소를 나눌때는 비워두고 만약 ,로 구분되어있다면 split(',') 이런 식으로 표기
    ```

- 리스트 정렬
  
  - ```python
    #1 sorted() 사용
    
    sorted([5, 2, 3, 1, 4])
    [1, 2, 3, 4, 5]
    
    #2 list.sort()
    
    a = [5, 2, 3, 1, 4]
    a.sort()
    a
    [1, 2, 3, 4, 5]
    
    #오름차순으로 정렬하고 싶다면
    bts_list = sorted(bts_list)
    bts_list.sort()
    
    #내림차순으로 정렬하고 싶다면
    bts_list = sorted(bts_list, reverse=True)
    bts_list.sort(reverse=True)
    ```

- 드래그 한 이후 `Ctrl + /` >> 주석처리

# 제어문
- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건) or 계속해서 실행(반복)하는 제어가 필요
- 제어문은 순서도로 표현 가능
<br><br>
## 조건문
- 참/거짓을 판단할 수 있는 조건식과 함께 사용
- 조건이 참일때 실행하는 코드블록/거짓일때 실행하는 코드블록을 지정
- ```python
  if 조건 == Ture:
    #Run this Code block
  else:
    #Run this Code block
- 실습 문제(num의 값이 홀수/짝수)
  - ```python
    num = int(input())
    if num % 2 == 0:
      print('짝수')
    else:
      print('홀수')
### 복수 조건문
  - elif 활용
- 실습 문제(num의 값이 홀수/짝수)
  - ```python
    dust = int(input())
    if dust > 150:
      print('매우나쁨')
    elif dust > 80:
      print('나쁨')
    elif dust > 30:
      print('보통')
    else:
      print('좋음')
    print('미세먼지 확인 완료')
### 중첩 조건문
  - 들여쓰기에 유의
  - ```python
    if 조건:
      #Code block
      if 조건:
        #Code block
    else:
      #Code block
### 조건 표현식
  - = 삼항 연산자
  - `true인 경우 값 **if 조건 else** false인 경우의 값`
  - `if 조건 else` 먼저 적고 값 양쪽에 적기
  - 실습 문제
    - ```python
      num = -5
      if num >= 0:
        value = num
      else:
        value = 0
      print(value)
<br><br>
## 반복문
- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
- while문
  - 종료조건에 해당하는 코드를 통해 반복문을 종료
- for문
  - 반복가능한 객체를 모두 순회하면 종료
  - 종료조건 따로 필요X
- 반복 제어
  - break, continue, for-else
### While문
- 조건식이 참인 경우 코드 반복 실행
- 무한 루프 하지 않도록 종료 조건 필요
- while 조건:
  - #Code block
- 복합 연산자
  - cnt += 1 의 `+=` 같은 것
  - 연산과 할당(저장)을 합쳐 놓은 것
### for문
- 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체의 요소를 모두 순회
- 종료조건 필요X
- 딕셔너리 순회시 key를 순회 >> 값을 활용
- ```python
    grades = {'john': 80, 'eric': 90}
    for student in grades:
      print(student, grades[student])
- keys(): key로 구성된 결과
- values(): value로 구성된 결과
- items(): (key, value)의 튜플로 구성된 결과
- enumerate 순회
  - 인덱스와 객체를 쌍으로 담은 열거형 객체 반환
  - (index, value) 형태의 튜플로 구성된 열거 객체를 반환
  - ```python
    members = ['민수', '영희', '철수']
    for idx, name in enumerate(members):
      print(idx, name) 
    print(list(enumerate(members)))
    """
    0 민수
    1 영희
    2 철수
    [(0, '민수'), (1, '영희'), (2, '철수')]
    """
- List Comprehension
  - `[code for 변수 in iterable]` #코드 부분이 리스트의 원소가 됨
  - `[code for 변수 in iterable if 조건식]`
    - ```python
      d_lst = [number ** 2 for number in range(6) if number % 2]
      print(d_lst)
      #[1, 9, 25]
- Dictionary Comprehension
  - `{key: value for 변수 in iterable}`
  - `{key: value for 변수 in iterable if 조건식}`
  - ```python
    dict_d = {number: number ** 2 for number in range(6) if number % 2}
    print(dict_d)
    #{1: 1, 3: 9, 5: 25}
    ```
    ```python
    lst = ['a', 'b', 'c']
    dict_lst = {num+1: lst[num] for num in range(3)}
    #dict_lst = {idx:value for idx, value in enumerate(lst,1)} 같은 결과
    print(dict_lst)

### 반복문 제어
- break: 반복문을 종료
- continue: 이후의 코드블록은 수행X, 다음 반복을 수행
- for-else: 끝까지 무사히 반복문을 수행한 이후에 else문 실행
  - break를 통해 중간에 종료되는 경우 else문 실행X
  - ```python
    for i in range(1, 6):
      if i < 10: #if i < 2:
        print(i ** 3)
      else:
        break
    else: print('끝')
    #현재 조건에서는 중간에 break가 발생하지 않음 > 1 8 27 64 125 끝
    #i < 2의 조건하에서는 중간에 break가 발생 > 1 만 출력
- while-else: for-else와 같은 방식
- pass: 문법적으로 필요하지만 할 일이 없을 때 사용 > 아무것도 하지 않음
<br><br>
<br><br>
# 함수
## 함수 기초
- Why?
  - Decomposition(분해)
    - 구구절절문을 간결하고 이해하기 쉽게!
  - Abstraction(추상화)
    - print 함수 어떻게 구현하는지 모르지만 사용할 수 있게!
### 함수의 종류
- 내장 함수
  - 파이썬에 기본적으로 포함된 함수
- 외장함수
  - import문을 통해 사용, 외부 라이브러리에서 제공하는 함수
- 사용자 정의 함수
  - 내가 만든 함수
### 함수의 정의
- 함수
  - 특정한 기능을 하는 코드의 조각(묶음)
  - 특정 코드를 매번 작성하지 않고 필요시에만 호출하여 간편히 사용
### 함수 기본 구조
- 선언(생성)
  - ```python
    def func_name(재료_parameters):
      """
      Docstring: 함수에 대한 설명
      어떤 기능을 위해 만들었고
      변수 무엇무엇을 받음
      주석처리 필수
      """
      #code block
      return returning_value #결과값 전달 #return 따로 써주지 않아도 항상 return하긴 함(return None이 생략되었다고 생각)
- 호출(사용)
  - 함수명()으로 호출
  - parameter 있으면 함수명(값1, 값2, )로 호출
  - ```python
    def add(x, y):
      return x + y
    #x, y라는 parameter가 있는 add 함수 선언
    add(2, 3)
    #호출 
- 문서화
<br><br>
## 함수의 입력
- parameter: 함수를 정의할 때, 함수 내부에서 사용되는 변수
- argument: 함수를 호출할 때, 넣어주는 값
  - parameter 자리에 들어가게 됨
  - 필수 argument
  - 선택 argument
  - Positional Arguments > Keyword Arguments 순으로 인식
    - 앞에서 Keyword Arguments를 인식했다면 뒤에 Positional Argument를 사용할 수 없음
  - Default Arguments Values
    - 함수 선언시 parameter 자리에 x=0 같은 형식으로 미리 기본값을 지정
    - 정의된 것보다 더 적은 개수의 argument로 호출될 수 있음
  - 가변인자(*args)
    - 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때 유용
    - `add()`
      - 입력받는 숫자를 갯수에 상관없이 다 더하고 싶음
      - ```python
        def add(*nums):
          s = 0
          for num in nums:
            s += num
          print(s)
      - 패킹
        - `numbers = 1, 2, 3, 4, 5`
      - 언패킹(시퀀스 속의 요소들을 여러개의 변수에 나눠 할당)
        - `a, b, c, d, e = numbers`
        - `for key, value in dic.items()`
    - 반드시 받아야하는 인자 / 추가적인 인자 구분 가능
      - ```python
        def print_family(father, mother, *pets):
          print(f'아버지: {father}')
          print(f'어머니: {mother}')
          for pet in pets:
            print(f'반려동물: {pet}')
        #함수 선언 완료
        print_family('아빠', '엄마', '보리', '치즈')
        """
        아버지: 아빠
        어머니: 엄마
        반려동물: 보리
        반려동물: 치즈
        """
  - 가변 키워드 인자(**kwargs)
    - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
    - 딕셔너리로 묶여 처리됨
    - ```python
      def family(**kwargs):
        for key, value in kwargs.items():
          print(key, ":", value)
      family(father= '아버지', mother= '어머니')
      #father : 아버지
      #mother : 어머니
    - 반드시 받아야하는 키워드 인자 / 추가적인 키워드 인자 구분 가능
      - ```python
        def print_family(father, mother, **pets):
          print('아버지 :', father)
          print('어머니 :', mother)
          for pet, name in pets.items():
            print(f'{pet} : {name}')
        #함수 선언 완료
        print_family('아빠', '엄마', 강아지= '보리', 고양이= '강양이')
        '''
        아버지 : 아빠
        어머니 : 엄마
        강아지 : 보리
        고양이 : 강양이
        '''
  - 가변 인자 / 가변 키워드 인자 동시 사용
    - ```python
      def print_family(*args, **pets):
        for arg in args:
          print('가족구성원 :', arg)
        for pet, name in pets.items():
          print(f'{pet} : {name}') #print('{} : {}'.format(pet, name)) 와 같은 결과
      #함수 선언 완료
      print_family('아빠', '엄마', 강아지 = '보리', 고양이 = '강양이')
      '''
      가족구성원 : 아빠
      가족구성원 : 엄마
      강아지 : 보리
      고양이 : 강양이
      '''
<br><br>
## 함수의 결과값
  - Void function
    - 명시적인 return 값이 없는 경우, None을 반환하고 종료
    - 파쇄기 같은 느낌 - 재료를 넣기는 했는데 나오는게 없음
  - Value returning function
    - 함수 실행 후, return문을 통해 값 반환
    - return을 하게 되면, 값 반환 후 함수가 바로 종료
    - print/return 차이점
      - print: 값을 출력 but 반환하지 않음, 호출될 때마다 값이 출력됨
      - return: 데이터 처리 목적 >> return 되는 값을 어떤 변수에 할당할 수 있음 a = len('bangtan')
    - 두 개 이상의 값을 반환하고 싶다면 tuple 사용
      - ```python
        def minus_and_product(x, y):
          return x - y, x * y

        y = minus_and_product(4, 5)
        print(y) #(-1, 20)
        print(type(y)) #<class 'tuple'> 
<br><br>
## 함수의 범위
- scope
  - global scope: 코드 어디에서든 참조할 수 있는 공간
  - local scope: 함수가 만든 scope. 함수 내부에서만 참조 가능
- variable
  - global variable: global scope에 정의된 변수
  - local variable: local scope에 정의된 변수
  - 변수마다 수명주기(lifecycle)가 존재
    - built-in scope: 파이썬이 실행된 이후부터 영원히 유지
    - global scope: 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - local scope: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
- 이름 검색 규칙
  - LEGB Rule(현재 위치보다 상위 스코프에 위치한 변수에 접근 가능하나 변경(해당 변수 이름에 다른 값 재할당)할 수 없음)
  - 컨테이너의 경우
    - 함수 내부에서 함수 바깥의 컨테이너 "안"의 값을 변경할 수도 있다.
  - ```python
    def f():
      lst = [1, 2, 3]
      def g():
        lst[0] = 3 #lst = [4, 5, 6] 으로 하면 최종 결과 [1, 2, 3]
      g()
    print(lst) #[3, 2, 3]
f()
    - Local scope
      - 지역 범위(현재 작업 중인 범위)
    - Enclosed scope
      - 지역 범위 한 단계 위 범위
    - Global scope
      - 최상단에 위치한 범위
    - Built-in scope
      - 정의하지 안하고 사용할 수 있는 모든 것
- global문
  - 하위 scope에서 global 변수 값 변경 가능하게 함
  - 하위 scope에서 global variable 생성도 가능(기존에 없던 변수에도 global 사용 가능)
  - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
  - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
    - ```python
      a = 10
      def func1():
        print(a) #global a 선언 전에 사용
        global a
        a = 3
      print(3)
      func1()
      print(a) #오류 발생
- nonlocal
  - global을 제외하고 가장 가까운 scope의 변수를 연결하도록 함(수정 가능하게)
  - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
  - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
  - global과는 달리 이미 존재하는 이름과의 연결만 가능함
<br><br>
## 함수 응용
- 내장함수
  - map(function, iterable)
    - 순회 가능한 데이터구조의 모든 요소에 함수 적용하고 그 결과를 map object로 반환
    - 결과 직접 확인하려면 리스트 형변환
    - 활용 사례
      - `n, m = map(int, input().split())`
  - filter(function, iterable)
    - 순회 가능한 데이터구조의 모든 요소에 함수 적용하고 그 결과를 filter object로 반환
    - 활용 사례
      - `odd_num = filter(odd, numbers)` #numbers는 리스트라고 가정
  - zip(*iterables)
    - 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
  - lambda 함수
    - lambda[parameter]: 표현식
    - return문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
    - def를 사용할 수 없는 곳에서도 사용가능
    - ```python
      triangle_area = lambda b, h : 0.5 * b * h
      print(triangle_area(5, 6)) #15.0
  - 재귀 함수
    - 자기 자신을 호출
    - 무한 호출 X, 점점 케이스가 줄어들다가 수렴하도록
    - 파이썬에서는 최대 재귀 깊이 1000번
    - 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨 << 이게 1000번이라고 생각하면 될듯
    - 대표적인 예시 팩토리얼 함수
    - ```python
      def f(n): #n이 1이상 자연수라고 가정
        if n == 1:
          return 1
        return n * f(n-1)
      print(f(5))
      ```
      ```python
      def s(n):
        if n == 1:
          return 1
        return n + s(n-1)
      print(s(10))
# 모듈
- import로 불러오기
  - import module
    - import requests 하면 requests 안의 get 함수를 쓰려면 requests.get()
  - from module import var, function, Class
  - from module import *
    - from requests import get 하면 get()으로 바로 사용가능
- 패키지 관리하기
  - `pip freeze > requirements.txt` : 지금 설치되어있는 패키지 목록 다 저장해줘~~
  - `pip install -r requirements.txt` : 저장해놨던거 다 깔아줘~~
<br><br>
# 가상환경
- why? 프로젝트마다 각자 필요한 환경이 달라서 이를 관리하기 위해
- how?
  ```python
  python -m venv venv #virtual environment
- 해당 가상환경에 깔려있는거...? 확인
  ```python
  source venv/Scripts/activate