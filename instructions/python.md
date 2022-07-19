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
