from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import BookSerializer, CustomUserSerializer, CommentSerializer, LikeSerializer
from .models import CustomUser, Comment, Like, Book

class CustomUserVIew(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAdmin]

class CommentVIew(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class BOokVIewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



@api_view(['GET'])

def get_like(request, book_id):
    book = Book.objects.get(pk=book_id)
    number_of_likes = Like.objects.filter(book=book).count()
    return Response({'likes':number_of_likes})

@api_view(['GET'])


def get_comment(request):
    book = Comment.objects.get('book_id')
    try:
        comment = Comment.objects.filter(blog=book)
    except Comment.DoesNotExist:
        return Response([])

    serializer = CommentSerializer(comment)
    return Response(serializer.data)