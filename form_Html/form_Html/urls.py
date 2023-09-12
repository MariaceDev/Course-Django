from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/form/', views.getForm, name='form'),
    path('get/goal/', views.getGoal, name='goal'),
    path ('post/form/', views.postForm, name= 'postGoal'),
    path ('post/goal/', views.postGoal, name= 'postGoal')
]
