from django.urls import path
from .views import *


urlpatterns = [
    path("", BookmarkListView.as_view(), name='list'), # name은 템플릿에서 사용할 url pattern 의 이름
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateview.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]