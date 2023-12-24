from django.urls import path
from .views import IndexView, RegisterPage, LoginPage, ProfileView, permission_denied_view
from . import views

app_name = 'app'

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path("register/", RegisterPage.as_view(), name='register'),
    path("login/", LoginPage.as_view(), name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("profile/update_player/<str:pk>/", views.update_player, name='update_player'),
    path("profile/update_contract/<str:pk>/", views.update_contract, name='update_contract'),
    path("profile/update_transfer/<str:pk>/", views.update_transfer, name='update_transfer'),
    path('profile/delete/<str:pk>/', views.delete_player, name='delete_player'),
    path('profile/delete/<str:pk>/', views.delete_contract, name='delete_contract'),
    path('profile/delete/<str:pk>/', views.delete_transfer, name='delete_transfer'),
    path('profile/delete/<str:model>/<str:pk>/', views.delete_object, name='delete_object'),
    path('permission_denied/', permission_denied_view, name='permission_denied'),

]
