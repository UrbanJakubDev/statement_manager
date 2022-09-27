from django.urls import path, include
from . import views


urlpatterns = [

   path('make_xml_message/', views.MakeXMLMessageView.as_view())
]