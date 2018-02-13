### **Part 3. Photo 앱과 모델 만들기**

*(1)Django Project와 App*

python 코드가 담긴 파일을 python 묘듈이라하고 python package는 파이썬 모듈을 묶어 놓은 단위. python  package는 초기화 모듈인 _ _init_ _.py 가 필요하다.

djagno를 이용하는 이유는 pystagram이라는  python package를 만들고 pystagram에 들어가는 기능은 python 모듈로 만든다는 의미.

*(2) Djagno project 만들기*

1. pystagram 디렉토리 생성 후 가상환경 진입

2. startproject pystagram 명령어 입력

   ```
   pystagram/
   |--manage.py
   |__pystagram
   	|--__init__.py
   	|--setting.py
   	|--urls.py
   	|__wsgi.py
   ```

   이러한 구성으로 파일이 생성된다.

   manage.py : Django로 돌아가는 프로젝트를 다양하게 다루는 도구.

3. cmder에  python manage.py createsuperuser 입력 후 ID,  PW를 입력하고python manage.py runserver 입력하면 웹에 로그인하는 창이 뜬다.

   ​

   *Django app, Photo app 구성*

   ```tree
   pystagram/
   |--db.sqlite3
   |--manage.py
   |--photos
   |	|--__init__.py
   |	|--admin.py
   |	|--apps.py
   |	|--migrations
   |	|	|___ __init__.py
   |	|--models.py
   |	|--test.py
   |	|__views.py
   |__pystagram
   	|--__init__.py
   	|--setting.py
   	|--urls.py
   	|__wsgi.py
   ```

   photos package = Django  App

   - admin.py : 관리자 영역에서 App을 다루는 코드를 담는 모듈
   - models.py : 모델을 정의하는 모듈
   - veiws.py : 특정  URL에 접근하면 화면에 내용을 표시하는 python 함수를 호출하는 내용을 담는다.

   ​

   *데이터베이스에 반영 시키기*

   1. settings.py에 들어가 INSTALLED_APPS 항목에 'photos' 입력

   2. python manage.py makemigrations -> ~~ migration 입력

      입력하면 DB에 반영된다.

      ​


   ​

