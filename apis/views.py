from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import response, request, generics
from .models import Movie, Platform
from rest_framework.decorators import api_view
from .seriallizers import MovieSerializer, PlatformSerializer
from rest_framework.views import APIView


class MovieListAV(APIView):
    
    def get(self,request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie,many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class MovieDetailsAV(APIView):
    
    def get(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    
    def put(self,request,pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()

        return Response("this is deleted")



    



# Create your views here.
# @api_view()
# def movies(request):
#      movie = Movie.objects.all()
#      serializer = MovieSerializer(movie, many =True)

#      return Response(serializer.data)

# @api_view()
# def movies_list(request, pk):
#      movie = Movie.objects.get(pk = pk)

#      serializer = MovieSerializer(movie)
#      if serializer.is_valid:
#           return Response(serializer.data)

# class PlatformList(generics.ListCreateAPIView):
#      queryset= Platform.objects.all()
#      serializer_class = PlatformSerializer

# class PlatformDetail(generics.RetrieveUpdateDestroyAPIView):
#      queryset = Platform.objects.all()
#      serializer_class = PlatformSerializer

