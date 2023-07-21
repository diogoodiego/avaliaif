from django.shortcuts import render
from django.contrib.auth.models import User
from avaliaif.models import Teacher, Review, Comment
from rest_framework import viewsets, permissions
from avaliaif.serializers import UserSerializer, TeacherSerializer, ReviewSerializer, CommentSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer