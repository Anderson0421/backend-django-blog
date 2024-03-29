from .views import *
from django.urls import path

urlpatterns = [
    path('list/posts',PostViewList.as_view(), name='post-list'),
    path('detail/<int:pk>/posts', PostDetailView().as_view(), name='post-detail'),
]
