from .views import *
from django.urls import path

urlpatterns = [
    path('list/posts',PostViewList.as_view(), name='post-list'),
    path('detail/<int:pk>/posts', PostDetailView().as_view(), name='post-detail'),
    
    #Cateogrias
    path('list/categories', ListCategoryView.as_view(), name='category-list'),
    path('filter/posts/<slug:slug>', FilterCategoryView.as_view(), name='filter-category'),
]
