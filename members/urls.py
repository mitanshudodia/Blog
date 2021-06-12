from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(),name = 'register'),
    path('edit_Profile/', views.UserEditView.as_view(),name = 'edit_setting'),
    path('password/', views.PasswordsChangeView.as_view(template_name = 'registration/change_password.html'),name = 'password_change'),
    path('password_success/', views.password_success,name = 'password_success'),
    path('<int:pk>/profile', views.ShowProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile', login_required(views.EditProfilePageView.as_view()), name='edit_profile'),
    path('create_edit_profile', login_required(views.CreateProfilePageView.as_view()), name='create_profile'),
]
    