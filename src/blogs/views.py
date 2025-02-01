from django.shortcuts import render

# Create your views here.
from blogs.models import Posts, Labels
from rest_framework import viewsets
from blogs.serializers import PostsSerializer, LabelsSerializer

class PostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class LabelsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Labels.objects.all()
    serializer_class = LabelsSerializer