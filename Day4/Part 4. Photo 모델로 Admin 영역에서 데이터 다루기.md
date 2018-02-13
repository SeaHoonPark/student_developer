#### **Part 4. Photo 모델로 Admin 영역에서 데이터 다루기**

1. Photo 모델로 데이터 넣기

   (1) Admin 에서 photo 모델 데이터 넣기

   - admin.py 관련 코드 작성

     - admin.site.register(Photo)

       admin package에 있는 sites 모듈에 Adminsite 클래스를 site라는 이름을 갖는 인스턴스를 만들고 이 site 객체의 인스턴스 매소드인 register로 지정한 모델을 Admin 영역에서 관리하도록 등록.

   => ~ runserver 입력 후 웹을 열고 PHOTOS라는 영역이 생성 => Photo 모델

   - 코드 중 blank=True 옵션이 있다. 빈칸을 허용하겠다는 뜻

     - 비슷한 옵션으로 null이 있다. null은 python의 None 자료형 객체를 뜻한다. 빈칸과 None은 의미가 다르다. 

       blank : 내용이 비어있는 문자형 객체로 None과는 DB의 테이블 구성도 달라 null=True라하면 해당 컬럼은 Null을 허용하도록 지정되고 blank=True만 있으면 null=True가 없어서 기본값인 null=False 로 지정되어 데이터베이스 테이블의 컬럼도 NULL이 허용되지 않는 NOT NULL로 지정된다.

2. 파일 업로드 경로 지정

   photo 모델이 데이터를 추가하면 업로드된 파일은 manage.py 파일에 저장된다. 업로드한 파일을 특정 지정 폴더로 변경하고 싶을 경우 특정 폴더를 가르키는 곳의 코드를 작성한다.

   1. ​	uploads/%Y/%m/%d/ 를 입력 시 년, 월, 일 순으로 업로드 한다.
      - 경로에 저장하는 %Y/%m/%d이런 문자열은 pythond의 strftime의 포맷팅에 사용되는 형태잡기 문자열 중에서 날짜와 시간과 같은 규칙을 따름.
      - 중간에 다른 경로로 폴더를 변경 가능하다.

3. 첨부 파일 삭제

   1. 모델을 삭제하는 기능이 호출되면 파일 삭제 기능도 실행

      - delete라는 인스턴스 메소드를 호출하여 모델 객체를 지운다. delete는 Model 클래스에 정의 되어있다. 

      1. def delete(self, *args, **kwargs):

         - delete 함수는 인스턴스 메소드이므로 첫째 인자로 객체 자신을 self라는 이름으로 넘겨 받는다. *args/ **kwargs는 함수가 넘겨받는 인자를 미리 알지 못하는 경우에 함수가 넘겨받는 인자를 담는 객체이다.

           ​

      2. self.image.delete()에서 self.image는 image 모델 필드를 뜻한다. 