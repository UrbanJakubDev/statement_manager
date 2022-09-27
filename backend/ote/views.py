from http.client import HTTPResponse
import os
from urllib import response
from django.shortcuts import render
import xml.etree.ElementTree as ET
from rest_framework import viewsets, generics, views
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse, FileResponse

from .services import XMLMessageBuilder

# Create your views here.


class MakeXMLMessageView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        # file absolute path to actual folder and file 'message.xml'
        file_path = './message.xml'
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

        builder = XMLMessageBuilder(
            sender_id="8591824556207",
            reciever_id="8591824000007",
            coding_scheme="14",
            sender_role='V')

        message = builder.make_message_body(
            year=year, month=month, units=units)

        with open('./message.xml', 'w') as f:
            f.write(message)

        # return succesful response
        response = FileResponse(
            open('./message.xml', 'rb'),
            content_type='application/xml'
        )
        return response
