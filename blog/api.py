#En este archivo API.py se creara la API para el modelo Post que se creo en el archivo models.py
from .serializers import PostSerializers
from .models import Post
from rest_framework import viewsets,permissions

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny]
    