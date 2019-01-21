from .models import Post
from django.contrib.auth.models import User
from rest_framework import serializers

# serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ('username',)

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post

        fields = ('title', 'content', 'timestamp', 'user', 'location')

