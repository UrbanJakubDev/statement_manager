from django.shortcuts import render

from django.contrib.auth.models import User, Group
from example_app.modules.xml_builder import XMLMessageBuilder
import xml.etree.ElementTree as ET

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
        return Response({'message': 'Hello, World!!!'})


class UploadFileView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        file = request.FILES['file']

        # return name of the file and its size

        return Response({'message': f'File {file.name} uploaded successfully'})


class MakeXMLMessageView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        year = 2022
        month = 8
        units = [
            {
                "idf": "019259_Z11",
                "ean": "859182400211637793"
            },
            {
                "idf": "034687_Z11",
                "ean": "859182400211958560"
            },
            {
                "idf": "034687_Z11",
                "ean": "859182400211958560"
            }
        ]

        builder = XMLMessageBuilder()
        message = builder.make_message(year=year, month=month, units=units)

        
        with open('./message.xml', 'w') as f:
            f.write(message)


        # return file and response message
        return Response({'message': f'XML message created successfully','raw_message': message})
