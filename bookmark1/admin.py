from django.contrib import admin

# Register your models here.
from .models import Bookmark

admin.site.register(Bookmark) # 북마크라는 모델을 등록시켜줘야 한다. 그리고 기능을 가져다 써야 한다.