# common/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'common'

urlpatterns = [
    # django.contrib.auth 앱의 LoginView 클래스 사용 
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]