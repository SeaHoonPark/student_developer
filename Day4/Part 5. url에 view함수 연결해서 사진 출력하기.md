### **Part 5. url에 view함수 연결해서 사진 출력하기**

(1) URL Resolver

user가 HTTP에 요청 -> url 확인 후 url에 연결된 함수 실행 -> views에서 models

를 이용해 데이터를 다룸 ->  views에서 (1)templates로 가거나 (2)직접 출력할 내용을 만듬 -> (1)일 경우 templates을 이용해 출력 할 내용을 만들어서 응답부로 전달 / (2)일 경우 직접 출력할 내용을 만든 후 출력물을 응받부로 전달 -> 요청한 HTTP에 전달

------

*요약*

1. `BaseHandler`가 URL로 요청 받음
2. `RegexURLResolver`로 URL을 보냄
3. `RegexURLResolver`가 URL에 연결된 View를 찾아서 callback 함수와 인자 등을 `BaseHandler`로 반환
4. `BaseHandler`에서 이 함수를 실행하여 결과값인 출력물을 받음.
5. 출력

------

해야할 기능 및 구현

1. Model이나 View에 기능 구현
2. user가 서버에 있는 자원에 접근하는 경로인 URL을 URL Dispatch 처리 모듈인 urls.py에 등록 후 URL에 구현부를 연결



**(1) view, urls**

views.py에 입력하고 싶은 문장을 입력한 후 웹에 접속하면 입력한 문장을 볼 수 있음

urls.py는 Django의 urls 모듈에 있는 url 함수를 이용하여 URL 연결자를 만들어서 urlpatterns에 넣는다.

주소 연결자를 만드는 url 함수는 총 4개 인자를 받는다.

- regex : 주소 패턴
- view : 연결할 view
- name : 주소 연결자 이름
- kwargs : urls에서 view로 전달할 dict 형 인자

regex 와 view는 필수 인자이다. urls.py에 입력한 코드 url(r'^hello/$', hello), 

를 예로 들면  regex = r'^hello/$'  , view = hello 이다.

view 인자는 실행할 함수 객체를 전달한다. 



2. photo 모델에서 사진 정보를 가져와 출력

   (1) photo 모델로 객체 찾기

   from .models import Photo 문으로 photos  앱에 있는  models 모듈에 Photo 모델을 가져온다. 

   (2) 찾는 객체가 없을 시 404 오류 출력

   from django.shortcuts import get_object_or_404 함수를 이용해 페이지를 따로 만든다. 

   (3) 업로드한 파일을 URL로 접근하기

   장고는 user가 업로드한 파일을  MEDIA_URL과 MEDIA_ROOT라는 설정값을 참조하여 제공한다. settings.py 파일에 맨 아랫줄에 두 설정값을 추가한다.

   ​

