from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializers

class PostViewList(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)