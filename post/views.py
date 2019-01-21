#from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Post
from django.contrib.gis.geos import Point
from website.utils import get_user_ip
from rest_framework import viewsets
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

class PostListViewSet(viewsets.ViewSet):
    """
    API endpoint that allows post to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class
    def list(self, request):
        # get user's location
        user_location = get_user_ip(self.request)
        user_point = Point(user_location['lon'], user_location['lat'], srid=4326)
        # query post by distance of user
        queryset = Post.objects.annotate(distance=Distance('location', user_point)).order_by('distance')
        print(str(queryset))
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
