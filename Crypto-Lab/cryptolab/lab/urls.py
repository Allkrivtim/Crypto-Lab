from django.urls import path
from .views import index, collect_dust

urlpatterns = [
    path('', index, name='index'),
    path('collect_dust/', collect_dust, name='collect_dust'),
]
