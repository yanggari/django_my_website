from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    #path('<int:pk>/',views.post_detail, name='detail')
    path('<int:pk>/', views.Postdetail.as_view(), name='detail'),
]