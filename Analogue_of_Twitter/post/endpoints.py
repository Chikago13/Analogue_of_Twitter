from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from rest_framework import viewsets


# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]

# class LikeListCreateView(generics.ListCreateAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     permission_classes = [IsAuthenticated]


class POstViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
