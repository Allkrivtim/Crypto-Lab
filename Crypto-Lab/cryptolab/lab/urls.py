from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('earn_tokens/', views.earn_tokens, name='earn_tokens'),
]
