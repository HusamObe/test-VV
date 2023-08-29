from rest_framework import generics
from .models import Comment, ChildComment
from .serializers import CommentSerializer, ChildCommentSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ChildCommentList(generics.ListCreateAPIView):
    queryset = ChildComment.objects.all()
    serializer_class = ChildCommentSerializer

class ChildCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChildComment.objects.all()
    serializer_class = ChildCommentSerializer
