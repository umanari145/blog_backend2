from blogs.models import Blogs, Labels
from rest_framework import serializers

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'contents', 'post_date', 'post_no', 'categories', 'tags']

class LabelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Labels
        fields = ['no', 'name', 'type']

