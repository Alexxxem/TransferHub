from django.urls import path
from .views import IndexView, RegisterPage, LoginPage, ProfileView
from . import views

app_name = 'app'

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path("register/", RegisterPage.as_view(), name='register'),
    path("login/", LoginPage.as_view(), name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("profile/update_player/<str:pk>/", views.update_player, name='update_player'),
    path('profile/delete/<str:pk>/', views.delete_player, name='delete_player'),

]
