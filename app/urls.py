from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('addpost/', views.addPost, name='addpost'),
    path('postdetail/<int:post_id>/', views.postDetails, name='postdetail'),

] 
