from .models import Post
from rest_framework import serializers

# serializers define the API representation.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'timestamp','location')

