from django.db import models

# Create your models here.
# 장고에서 모델이란 ORM이란 기능을 통해서 프로그래머가 SQL을 몰라도 데이터베이스를 사용할 수 있도록 도와준다.
# Object Relation Management라는 것으로 장고에서는 DB와 클래스를 맵핑해주는 놈...
# models.Model이 실제적인 기능 함수를 가지고 있다.
# 모델까지 만들었을 경우라면 아직 DB에 반영 안된 상태임
# --> 기록하려면 makemigrations, migrate를 이용해야 한다
# python manage.py makemigrations bookmark1
# python manage.py sqlmigrate bookmark1 0001
# python manage.py migrate bookmark1 0001
# 데이터베이스에 직접 접근하는 방법 : python manage.py dbshell
# 데이터베이스에 간접 접근하는 방법(모델을 이용해서) : python manage.py shell

class Bookmark(models.Model): # DB를 사용하려면 무조건 포함되어야 하는 코드

    # 클래스 변수, 속성 : 데이터베이스 컬럼
    # 필드 종류 : 문자열, 숫자, 불린, 바이너리
    # 각 ㅣㄹ드의 제약 조건 : 컬럼의 제약 조건
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 위 내용은 북마크라는 컬럼에 사이트_이름과 url이라는 필드가 있고 아래의 옵션이 있다고 생각하면 됨

    # 필드 종류 : 프론트 페이지에서 어떤 폼 태그를 사용할 거신지, 폼 태그에서 제약 조건

    def __str__(self):
    # 객체를 출력할 때 나타날 값
        return self.site_name + " aaa : " + self.url
    # 모델 내부의 메서드 들은 필드처럼 사용할 수 있다.
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.id)])
    # 다양한 정보를 갖는 클래스
    class Meta:
        ordering = ['site_name']