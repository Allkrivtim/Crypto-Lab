from django.urls import path
from . import views

urlpatterns = [
    path('lab/', views.index, name='index'),
    path('lab/collect_dust/', views.collect_dust, name='collect_dust'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
]
