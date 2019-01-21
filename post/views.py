#from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Post
from django.contrib.gis.geos import Point
from website.utils import get_user_ip
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer

class PostListView(ListView):
    model = Post
#    context_object_name = 'posts'
    template_name = 'post/index.html'   

    def get_context_data(self, **kwargs):
        user_location = get_user_ip(self.request)
        user_point = Point(user_location['lon'], user_location['lat'], srid=4326)
        context = super().get_context_data(**kwargs)
        context['posts'] =  Post.objects.annotate(distance=Distance('location', user_point)).order_by('distance')
        print(str(context['posts']))
        return context

@api_view(['GET'])
def PostListAPI(request):
    """
    API endpoint that list post to be viewed.
    """
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def get_queryset(request):
        """
        query post by distance
        """
        # get user's location
        user_location = get_user_ip(request)
        user_point = Point(user_location['lon'], user_location['lat'], srid=4326)
        return Post.objects.annotate(distance=Distance('location', user_point)).order_by('distance')
