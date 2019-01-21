from .models import Post
from rest_framework_gis.serializers import GeoFeatureModelSerializer

# serializers define the API representation.
class PostSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Post
        geo_field = 'location'
        fields = ('title', 'content', 'timestamp')

