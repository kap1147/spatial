from django.urls import path, include
from . import views
#from .models import Post
#from rest_framework import routers, serializers, viewsets
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

"""
# Serializers define the API representation.
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'timestamp')

# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Routers provided an easy way of automatically determinig the URL conf.
router = routers.SimpleRouter()
router.register(r'post', views.PostListViewSet, basename='post') 
"""

app_name='posts'

urlpatterns = [
    path('', views.PostListView.as_view()),
#    path('api', include(router.urls)),
    path('api/posts/', views.PostListAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
