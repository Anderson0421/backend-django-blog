from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from .models import Post, Category
from .serializers import PostSerializers,CategorySerializers

class PostViewList(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)

class PostDetailView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, pk , format=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializers(post)
        return Response(serializer.data)
        
class ListCategoryView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        categorias = Category.objects.all()
        serializer = CategorySerializers(categorias, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)   

class FilterCategoryView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request,slug, format=None):
        categorie = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=categorie)
        serializer = PostSerializers(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        