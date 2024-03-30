from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content','bg_image','excerpt')
        read_only_fields = ('created_at', 'updated_at')
