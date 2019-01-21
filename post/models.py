from django.contrib.gis.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    location = models.PointField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title
