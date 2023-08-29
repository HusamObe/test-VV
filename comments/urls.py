from django.urls import path
from .views import CommentList, CommentDetail, ChildCommentList, ChildCommentDetail

urlpatterns = [
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('child-comments/', ChildCommentList.as_view(), name='child-comment-list'),
    path('child-comments/<int:pk>/', ChildCommentDetail.as_view(), name='child-comment-detail'),
]
