**Python 가상환경**

가상환경 생성 = python -m venv myvenv(원하는 가상환경 이름)

가상환경 진입 = myvenv\Scripts\activate.bat

가상환경 빠져나오기 = deactivate

| 명령    | 설명                      |
| ----- | ----------------------- |
| ls    | 디렉터리 목록을 보여줌.           |
| mkdir | 디렉터리를 생성함.              |
| rm    | 파일 혹은 디렉터리를 지움.         |
| mv    | 파일을 이름을 변경하거나 옮길 때 사용함. |
| pwd   | 현재의 위치를 출력.             |



**Sequence 슬라이싱**

한 Sequence에서 Sequence의 일부를 추출 가능.

-[start:end:step]을 명시하여 슬라이스를 정의.

-start 오프셋을 명시하지 않으면 0 / end오프셋을 명시하지 않으면 마지막 인덱스.

-step은 어떻게 이동할 것인지 명시.

**리스트**

- 다양한 숫자형 입력가능

- 변경 가능한 객체

  ​

**튜플**

- 상수 리스트

- 변경 불가능한 객체

  ​

패킹 = 여러 항목을 리스트나 튜플에 넣는 것

언패킹 = 리스트나 튜플에 있는 항목을 변수들로 풀어헤쳐 담는 것 

[info='James','male',27]

[name,gender,age=info]

[name,gender,age='James','male',27]



**조건문**

다른 언어와 달리 if조건 테스트에는 괄호가 필요없고 콜론을 사용

------

```python
if a == b and a > 0:
    pass
elif a != b or b < 0:
    pass
else:
    pass
```

```python
for [한 요소] in [반복가능한 객체]:
    [실행 내용]
```

```python
while[조건]:
     [실행 내용]
- 조건식이 참인 한 블럭 내 구문을 계속 반복
```

**컴프리헨션**

비교적 간편한 구문으로 조건문과 반복문을 결합할 수 있도록 해줌

리스트 컴프리헨션

[표현식 for 항목 in 순회 가능한 객체]



| 반복문 예시              | 리스트 컴프리헨션 예시                         |
| ------------------- | :----------------------------------- |
| list1 = []          | list2 = \                            |
| for i in range(10): | [x for x in range(10) if x % 2 == 0] |
| if i % 2 == 0:      |                                      |
| list1.append(i)     |                                      |



**함수 표현**

```
def [함수 이름](매개변수):
    [실행 내용]
    return [반환]
```



```
ex)
def greet(name):
    print('{}님 안녕하세요'.format(name))
    return True
is_greet = greet('Pando')
```

------

*함수의 구성요소*

순서 1) 인자,2)위치인자,3)키워드인자

위치인자 = 함수의 매개변수를 튜플로 묶기 위해 애스터이스크(*)를 사용

= 인자 이름을 지정하지 않고 차례로 나열

```
def print_args(*args):
    print('Positional arqument:',args)
print_args(1,2,'as',{'a':1,'b':2},[1,2])
```

키워드 인자 = 함수의 매개변수를 딕셔너리로 묶기위해 두개의 애스터리스크(**)를 사용

= 인자 이름을 지정하고 차례로 나열

```
def print_kwargs(**kwargs):
    print('Keyword arguments:',kwargs)
print_kwargs(animal='cat',fruit='apple')
```

------

모듈(python 파일) && 패키지(파일 디렉토리)

- python 어플을 좀 더 확장 가능하게 만들기 위해 모듈을 패키지라는 파일 계층구조에 구성
- 디렉토리에 파일 이외에 필요한 파일이 있는데, _init_.py파일 python은 이 파일을 포함하는 디렉토리를 패키지로 간주

------

객체 && 클래스

객체 = 클래스를 실체화 한것.(데이터와 코드를 모두 포함)

클래스 = 파이썬은 모든 자료형이 객체 / 객체는 자료형(type) 으로부터 만듬

*클래스는 새로운 객체 자료형을 정의하는 자료형*

------

Decorator = 함수를 꾸며주는 함수(기존 함수에 기능을 추가, 새로운 함수를 만듬)

**Iterable / Iterator**

- Iterator란 반복가능한 Iteralbe의 객체 중 하나
- Iterator는 next()메소드가 있는 실행 가능한 객체
- next()의 마지막은 StopIteration 예외 발생

**Generator**

- yield문이 있으면 모두 Generator
- 순환할 때마다 필요한 값을 만들어 값을 발생시킴, 함수 안에서 특정 지점에서 진행을 잠시 멈추고 나중에 다시 그 위치에 진입
- StopIteration 예외 오류를 일으키면 종료

```
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr
```

------

**Git && Github**

Git의 구조

```sequence
Working Directory -> Staging Area: Stage Fixes
Staging Area -> .git directory(Repository):Commit
.git directory(Repository) -> Working Directory:Check the project
```

1. Working Tree에서 파일을 수정
2. Staging Area에 파일을 Stage해서 커밋할 스냅샷을 만듬
3. Staging Area에 있는 파일들을 커밋후 Git디렉토리에 영구적인 스냅샷으로 저장

Git : 분산형 버전관리 도구

Github : 버전관리 시스템인 Git을 이용하는 프로젝트들을 위한 원격저장소를 제       공하는 서비스

Git 용어

| Git 용어          | 설명                                       |
| --------------- | ---------------------------------------- |
| git init        | git을 시작함.                                |
| .gitignore      | local에서만 사용되고 repository에 올라가지 않는다. git 버전관리에 표함되고 그 파일안에 있는 내용은 추적되지 않는다. |
| git remote      | 명령으로 현재 프로젝트에 등록된 리모트 저장소를 확인할 수 있다.     |
| git add         | commit 즉 버전을 만들기전에 꼭 해야하며 파일을 추적하게 되는것.  |
| git commit      | 버전을 생성시켜준다.                              |
| git status/diff | 현재 git에 보관된 파일들을 생성한다. ///주소..주소: 내가 입력한 주소들 간의 버전 차이를 알려준다. |
| git push/pull   | 원격저장소에 push해서 올린다 / github에 있는 코드를 pull로 가져온다. |
| git log         | 버전 정보들을 볼 수 있다. 언제 버전을 바꿔 줬는지            |
| git branch      | branch 목록을 볼때, 생성할 때 git branch "branch name" |
| git checkout    | branch를 전환/체크아웃할때 //전환할때에는 git checkout "전환하려는 브랜치 이름" |
| git merge       | 브랜치를 병합할 때 사용.                           |
| git stash       | 워킹 디렉토리에 unstaged 파일들을 백업하고 워킹디렉토리를 깨끗한 상태 즉 HEAD의 상태로 만드는 것이다. |
| git clone       | 다른 프로젝트에 참여하거나(Contribute) Git 저장소를 복사하고 싶을 때 git clone 명령을 사용한다. |

##### 