from http.client import HTTPResponse
import os
import pprint

from django.shortcuts import HttpResponse
from .models import Unit
from rest_framework import views
from rest_framework import permissions
from rest_framework.response import Response
from django.http import FileResponse
import pandas as pd

from .services import XMLMessageBuilder

# Create your views here.


class MakeXMLMessageView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        year = int(request.GET.get('year'))
        month = int(request.GET.get('month'))
        units_limit = int(request.GET.get('units-limit'))

        # Initiate XMLMessageBuilder class
        builder = XMLMessageBuilder(
            sender_id="8591824556207",
            reciever_id="8591824000007",
            coding_scheme="14",
            sender_role='V')

        # Query units from database
        units = Unit.objects.all().values('idf', 'ean')

        # Generate XML files
        builder.generate_xml_files(year, month, units, units_limit=units_limit)
        builder.generate_zip_file('files.zip')

    
        file_memory = open('files.zip', 'rb')
        response = FileResponse(file_memory, as_attachment=True, filename='files.zip')
        return response


# Only for testing purposes
# View to load Units from csv file to database
class LoadUnitsView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        items = pd.read_csv('./units.csv')

        for index, row in items.iterrows():
            unit = Unit(
                idf=row[1],
                ean=row[0]
            )
            unit.create()

        return Response({'status': 'success'})
