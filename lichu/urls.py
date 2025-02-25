from django.urls import path
from .views import lichu_list

urlpatterns = [
    path('', lichu_list, name='lichu_list'),
]
