from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name='home'),
    path('sign', views.sign, name='sign'),
    path('log', views.log, name='log'),
    path('direct', views.direct, name='direct'),
    path('stories', views.story, name='story'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit, name='edit'),
    path('logout', views.logout, name='logout'),
    path('profile/post', views.post, name='post'),
]