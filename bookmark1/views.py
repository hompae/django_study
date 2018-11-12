from django.shortcuts import render

# Create your views here.

# MTV : 디자인 패턴
# 디자인 패턴 : 설계 상의 문제를 해결하기 위해 나온 방법
# M : Model - 데이터베이스를 쉽게 사용하려고
# T : Template - html 같은 프론트 코드.. 디자인을 바꾸고 싶다.
# V : view - 로직, 기능 같은 백엔드 코드...서버에서 돌아가는 로직을 만들고 싶을 때...
# 위 세 가지는 쌍으로 돌아간다.

# 리스트 페이지를 만들고 싶다면...
# 데이터베이스에서 북마크를 불러온다. - 모델이 한다
# 해당 북마크를 템플릿에 넣어 가공한다. - 로직이 처리
# 가공한 결과 코드를 사용자(브라우저)에게 전달한다. - 로직이 처리
# 위 세가지 일은 실제 view 안에서 이루어진다....뷰가 모델을 불러오는 것이라서 뷰 안에서 다 이루어진다는 의미

# 뷰 : 두 종류
# 클래스형 뷰 : class 형태 - 언제? 보통 하는 일을 하고 싶을 때..
# 보통 하는 일을 하는 뷰는 장고에서 이미 만들어 뒀다. Generic view 라고 한다...Class Based View 라고 한다...클래스라 상속을 받아서 사용해야 한다.
# CRUD 역할이며 장고에서 미리 만들어 둔 것...
# 함수형 뷰 : def 형태 - 언제? 내가 혼자 지지고 볶고 할 때..

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView # 얘가 CRUD에서 R에 해당하는 view 이다.

# 클래스형 뷰를 사용할 때도 옵션은 존재...어디를? 몇 페이지를?
# 함수형 뷰에서는 많은 내용을 다룰 예정이고 클래스는 옵션을 활용할 것이다.

from .models import Bookmark
class BookmarkListView(ListView): # Listview 를 상속받은 형태. 뷰 이름은 아무 이름이나 지을 수 있다.
    model = Bookmark # Bookmark에 처음에는 붉은 줄이 생길 것이다. 안가져 왔으니까..위에 import 해 준다.
    paginate_by = 3

from django.urls import reverse_lazy
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') # 글쓰기를 완료했을 때 이동할 페이지...
    template_name_suffix = '_create'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkDeleteView(DeleteView):
    model = Bookmark