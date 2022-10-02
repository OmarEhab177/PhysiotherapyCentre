from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserView, signup, login_view

from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    # path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login', login_view, name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('profile/', login_required(UserView.as_view()), name='profile'),
    # path('signup', signup, name='signup')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
