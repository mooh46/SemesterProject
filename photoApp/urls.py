from django.urls import path
from . import views


urlpatterns = [
path('',views.log_in,name='login'),
path('register',views.register,name='register'),
path('feed',views.feed,name='feed'),
path('logout',views.log_out,name='logout'),
path('new_post',views.new_post,name='new_post'),
path('profile/<int:user_id>',views.profile,name='profile'),

]