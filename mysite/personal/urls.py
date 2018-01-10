from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.addpost, name='addpost'),
    path('postlist',views.postlist, name='postlist'),
    path('inbox',views.inbox, name='inbox'),
]