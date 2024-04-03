from rest_framework import serializers
from .models import Post, Category

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content','bg_image','excerpt')
        read_only_fields = ('created_at', 'updated_at')

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug','id', 'name')
