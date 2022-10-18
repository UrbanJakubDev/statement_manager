from django.urls import path, include
from . import views


urlpatterns = [

   path('make_xml_message/', views.MakeXMLMessageView.as_view()),
   path('parse_xml_message/', views.ParseXMLMessageView.as_view()),
   path('load_units/', views.LoadUnitsView.as_view())
]