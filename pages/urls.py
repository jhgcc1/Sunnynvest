
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import login , urls
urlpatterns = [
    url(r'^teste/(?P<var>[-\w]+)/$', views.teste, name='teste'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('input/', views.input, name='input'),
    url(r'^login/$', views.login, name="login"),
    url(r'^register/$', views.register, name="register"),
    path('passchanged/', views.testpage, name='testpage'),
    path('profile/', views.profile, name='profile'),
    path('logoutt/', views.logoutt, name='logout'),
    url(r'^login2/$', views.login2, name="login2"),
    path('fgtpass/', views.fgt, name='forgotpassword'),
    url(r'^password_reset/$', PasswordResetView.as_view(template_name='forgotpassword.html',email_template_name='emailfgtpassword.html',subject_template_name='subjectemailfgtpassword.html'), name='ps'),
    url(r'^password_reset/done/$',PasswordResetDoneView.as_view(template_name='passwordresetsent.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(template_name='forgotpassword2.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='forgotpassword3.html'), name='password_reset_complete'),
   ]