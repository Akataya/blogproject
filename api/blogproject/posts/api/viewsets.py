from ..models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    # List, create, retrieve, update, partial_update, destroy
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    # List, create, retrieve, update, partial_update, destroy
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

