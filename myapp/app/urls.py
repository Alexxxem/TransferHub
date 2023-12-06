from django.urls import path
from .views import IndexView, RegisterPage, LoginPage
from . import views

app_name = 'app'

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("register/", RegisterPage.as_view(), name='register'),
    path("login/", LoginPage.as_view(), name='login'),
]