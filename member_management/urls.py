from django.urls import path
from . import views

urlpatterns = [
    path('mno/', views.home2),
    path('abc/',views.home4,name='members-list'),
    path('',views.home5,name='auto-forms')
    
]