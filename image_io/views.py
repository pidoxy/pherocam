from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework.response import Response
from .models import Images

# Create your views here.

class ImageIO(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

class RetrieveImageIO(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer