### Part 2. 개발 환경 꾸리기

1. Python 설치

2. pip 설치 

   1. pip :  python에 사용되는 각종 패키지를 설치하거나 업그레이드, 삭제 등을 관리하는 도구.

3. 가상 환경 만들기

   1. python -m venv myvenv

4. SQLite 설치

   1. 데이터를 저장하는데 필요한 DB는 SQLite를 사용

5. Django 설치

   1. 가상환경 진입
      - myvenv\Scripts\activate.bat
   2. Django 설치 
      - pip install django
      - python -c "import django; print(django._file_)" => 설치 되었는지 확인
   3. 편집기 사용(PyCharm)​