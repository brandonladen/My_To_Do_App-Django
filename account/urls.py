from django.urls import path
from .views import login_user, logout_user, signup, view_profile, edit_profile
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('login/', login_user, name='login'),
    path('login/', logout_user, name='logout'),
    #path('login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name="login"),
    path('signup', signup, name='signup'),
    path('profile/', view_profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]