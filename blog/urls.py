from .views import *
from django.urls import path

urlpatterns = [
    path('list/posts',PostViewList.as_view(), name='post-list'),
]
