# 처음에 비어있고...

from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/ 를 의미하려면 '' 를 url패턴에..입력
    # 함수형 뷰 : 뷰 이름만 쓴다.
    # 크래스형 뷰 : 뷰이름.as_view()
    path('', BookmarkListView.as_view(), name='list'), # path는 3개를 입력 받는데 실상은 4개이다. url패턴, 뷰, url 패턴의 이름,
    # BookmarkListView는 클래스라 .as_view()를 덧 붙여줘야 한다. 여기있는 urls.py에 외부에서 바로 접속이 되질 않는다. 외부에서 접속하면 상위 앱인 bookmark에 있는 urls.py를 참조하므로 해당 파일에 있는 내용을 연결시켜 줘야 한다.
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
    ]