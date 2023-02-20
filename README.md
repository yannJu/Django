# Django💻
1. [1_startDjango](./1_startDjango/)
   - Conda 환경에서 Django 실행해보기🩹
   - manage.py 에서 명령 실행
   - config 가 패키지 처럼 ! 하위 파일은 모듈처럼 !
   - "앱단위"로 기능 추가 및 관리 
     - django-admin startapp "앱 명" : 앱추가
     - config > *setting.py* > INSTALLED_APPS 에서 새로운 앱이 연동되도록 설정
     - config > *urls.py* > urlpatterns 에서 django 가 처리할 수 있는 url 나타냄
      - 앱 단위로 url을 분리하여 관리하는 것을 권장
    - settings 내에서 두가지를 수정
      - settings > LANGUAGE_CODE = **'ko-kr'**
      - settings > TIME_ZONE = **'Asia/Seoul'**
2. [2_Django_DB](./2_Django_DB/)
   - 데이터 베이스 연동하기🛍
   - "SQLite" 를 이용하여 연동
     - python manage.py **migrate** 를 이용하여 migrate
     - python manage.py **createsuperuser** 를 이용하여 superuser 생성
   - admin 로그인 및 접속 가능
3. 