> 2020.01.13 월

### 이번주 과정

- 파이썬 기초
- 크롤링, 데이터 분석
- 자연어 처리
- 챗봇 만들기
- 형상관리 Github



# Python

- 프로그래밍 언어 중 하나
- 1991년 Guido Van Rossum에 의해 개발됨
- 인터프리터 언어

### 왜 파이썬인가?

- 개발 생산성이 높음
- 세계적으로 가장 대중적인 언어 중 하나
- 다양한 라이브러리 제공
- 높은 범용성
  - 일반 어플리케이션
  - 웹 프로그래밍
  - 데이터 분석
  - 인공지능
  - GUI 개발



[Google **Colab**](https://colab.research.google.com/)

- 클라우드에서 실행되는 무료 Jupyter 노트 환경

---

#### 데이터 타입 Data type

- 숫자형 : int, float, complex
- 문자열 : str
- Boolean : bool
- 시퀀스 : list, tuple, set
- 맵 : dict

####  연산자

- 산술 연산자
  - // - 소수점 버림 나눗셈 연산자
  - % - 나머지 연산자
  - ** - 제곱 연산자

#### 문자열

- 문자열 포맷

  - 문자열에 숫자 또는 문자열을 대입
  - % 연산자

  ```python
  print("Are you %s?" % "Emma")
  print("I'm %d years old" % 26)
  print("%d * %d = %d" % (3,4,3*4))
  ```
  - format()

  ```python
  print("My name is {}" .format("Jone"))
  print("{} * {} = {}" .format(3,4,3*4))
  ```

- 문자열 교체

  ```python
  txt = "Hi, Kim!"
  print(txt.replace("Hi", "Hello")) # Hello, Kim!
  ```

- 문자열 공백 없애기 : strip(), rstrip(), lstrip()

  ```python
  txt = ' python '
  print(txt.strip()) # 양쪽 문자열/공백 제거
  print(txt.rstrip()) # 오른쪽 문자열/공백 제거  
  print(txt.lstrip()) # 왼쪽 문자열/공백 제거
  ```

-  문자열 체크 : in, not in

  ```python
  txt = "I have some apples and bananas"
  print("app" in txt) # True
  print("bana" not in txt) # False
  ```

#### 조건문

- pass : 어떤 작업도 실행하지 않음

#### 리스트

- 특정한 순서로 연결되어 있는 데이터의 집합
- 숫자, 문자열, 리스트 등 다양한 종류의 데이터를 넣을 수 있음
- 대괄호 기호를 이용하여 생성 - [ ]

- 리스트 slicing 

  - 서브 리스트로 만듦
  - start : end (: step) 형식

- step 지정

  ```python
  nums = [1,0,6,5,4]
  print(nums[::2]) # [1,6,4]
  print(nums[::-1]) # [4,5,6,0,1]
  ```

- 항목 추가

  ```python
  nums = [1,0,6,5,4]
  nums.append(123)
  print(nums) # [1,0,6,5,4,123]
  nums.insert(0, 33)
  print(nums) # [33,1,0,6,5,4,123]
  ```

- 항목 제거

  ```python
  nums = [1,0,6,5,4]
  del nums[0]
  print(nums) # [0,6,5,4]
  popped_nums = nums.pop()
  print(nums) # [0,6,5]
  print(popped_nums) # 4
  nums.remove('0') 
  print(nums) # [6,5]
  ```

- 리스트 합치기

  - '+' 연산자
  - extend()

- 정렬

  ```python
  # sort()
  cars = ['hyundai', 'bmw', 'audi', 'toyota']
  cars.sort()
  print(cars) # ['audi', 'bmw', 'hyundai', 'toyota']
  cars.sort(reverse=True)
  print(cars) # ['toyota', 'bmw', 'hyundai', 'audi']
  cars.sort(key=len)
  print(cars) # ['bmw', 'audi', 'toyota', 'hyundai']
  # sorted()
  print(sorted(cars)) # ['audi', 'bmw', 'hyundai', 'toyota']
  # reverse
  cars = ['hyundai', 'bmw', 'audi', 'toyota']
  cars.reverse()
  print(cars) # ['toyota', 'audi', 'bmw', 'hyundai']
  ```

- 값의 개수 세기

  ```python
  cars = ['hyundai', 'bmw', 'audi', 'toyota']
  print(cars.count('bmw')) # 1
  ```

- range 함수

  ```python
  a = ragne(3)
  print(list(a)) # [0,1,2]
  print(list(range(0,10))) # [0,1,2,3,4,5,6,7,8,9]
  print(list(range(0,10,2)) # start, end, step [0,2,4,6,8]
  print(list(range(5,0,-1))) # [5,4,3,2,1]
  ```

- 통계함수

  ```python
  digits = [1,2,3,4,5,6,7,8,9,0]
  print(min(digits)) # 0
  print(max(digits)) # 9
  print(sum(digits)) # 45
  ```

- 복사 : soft copy

  ```python
  x = ["a", "b", "c"]
  y = x
  y[1] = "z"
  print(y) # ["a", "z", "c"]
  print(x) # ["a", "z", "c"]
  ```

  ```python
  a = [1,2,3]
  b = a
  c = a[:]
  d = list(a)
  # a는 b와 같지만 c, d와는 다르다
  # b는 새로 생성된 list가 아님
  # c와 d는 새로 list가 생성된 것
  ```

#### 반복문

- for
- while
- break
- continue

#### 튜플

- 순서가 있음

- ( ) 기호를 사용하거나 생략

  ```python
  items = ("ruler", "pen", "eraser")
  nums = 1,2,3
  ```

- 각 슬롯에 저장된 값을 재할당 불가

- 문자열이나 리스트 등을 튜플로 변환 : tuple()

  ```python
  tup1 = tuple("python")
  print(tup1) # ('p','y','t','h','o','n')
  tup2 = tuple([1,2,3])
  print(tup2) # (1,2,3)
  ```

- 인덱스로 각 원소에 접근

- 패킹/언패킹

#### 딕셔너리

- Key/ Value 형태의 자료구조

- Key 값으로 Value를 조회 가능

- 리스트와 혼합 된 형태로 사용 가능

- { } 기호를 사용하여 생성

  ```python
  alien = {'color':'green', 'points':5}
  print(alien['color']) # green
  print(alien['points']) # 5
  ```

- 딕셔너리 항목 제거

  ```python
  alien = {'color':'green', 'points':5}
  del alien['points']
  print(alien) # {'color':'green'}
  c = alien.pop('color')
  print(c) # green
  print(alien) # {}
  ```

- 딕셔너리 key/value 접근

  ```python
  alien = {'color':'green', 'points':5}
  alien_keys = list(alien.keys())
  print(alien_keys) # ['color', 'points']
  alien_values = list(alien.values())
  print(alien_values) # ['green', 5]
  ```

- 딕셔너리 looping

  ```python
  thisdict = {
  	"brand": "Ford",
  	"model" : "Mustang",
  	"year" : 1964
  }
  print(thisdict) # {"brand": "Ford", "model": "Mustang", "year": 1964}
  # key 정보 출력
  for x in thisdict:
      print(x) # brand model year
  # value 정보 출력
  for x in thisdict:
      print(thisdict(x)) # Ford Mustang 1964
  for x in thisdict.values():
      print(x) # Ford Mustang 1964
  # key, value 정보 출력
  for x,y in thisdict.items():
      print(x,y) # brand Ford  model Mustang  year 1964
  ```

#### 함수

- 이름이 붙여진 코드의 블록
- 특정한 태스크를 반복 수행 가능
- 입력과 출력이 존재
  - 입력 - 파라미터
  - 출력 - 리턴값
- 다른 코드에서 사용 될 수 있음 : 함수 호출

- 함수의 선언과 호출, 파라미터 사용

  ```python
  def greet_user(username):
  	print("Hello, " + username + "!")
  greet_user('Jone') # Hello, Jone!
  ```

- 가변인자 : 임의의 개수의 인자를 넘기기

  ```python
  def make_pizza(*toppings):
  	for topping in toppings:
  		print("- "+topping)
  make_pizza('mushroom', 'green peppers', 'extra cheese')
  /*
  - mushroom
  - green peppers
  - extra cheese
  */
  ```

  

## 데이터 크롤링

#### 크롤링 기술이란?

- 프로그래밍 언어를 통해 인터넷에서 우리에게 필요한 정보를 빠르고 정확하게 수집할 수 있는 방법











