from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins


from .serializers import PostSerializer
from .models import Post


"""
The 3 classes below all do the same thing.
notice the high level of abstraction in the 3rd class > 2 > 1.
This is possible with the use of mixins.
"""
# Create your views here.
class PostView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


"""
#This function exists in mixins.py. here we are overwriting that function to accomplish some functionality(here, sending an email)
    def perform_create(self, serializer):
        #send and email(basically here we can add the functioanlity of what we want to do)
        serializer.save()
"""

"""
class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        #serializer = PostSerializer(qs, many = True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
"""

"""
def test_view(request):
    data = {
        'name': 'john',
        'age':23
    }
    return JsonResponse(data)
"""
