from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog',views.blog ,name= 'blog'), 
    path('profile',views.profile, name = 'profile'),
    path('about',views.about, name='about'),
    path('post',views.post, name = 'post'),
    path('',views.home, name='home'),
    path('signup',views.signup,name = 'signup'),
    path('login',views.login_page, name = 'login')


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)