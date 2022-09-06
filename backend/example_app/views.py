from django.shortcuts import render

from django.contrib.auth.models import User, Group

from rest_framework import viewsets, generics, views
from rest_framework import permissions
from rest_framework.response import Response



from .serializers import UserSerializer, GroupSerializer

# Create your views here.


def index(request):
    return render(request, 'index.html')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


    
class ExampleView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({'message': 'Hello, World!'})