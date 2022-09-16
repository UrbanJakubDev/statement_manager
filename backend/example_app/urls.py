

from django.urls import path, include
from . import views

urlpatterns = [

    # Path to the index view
    path('home/', views.index, {}),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # Test path to the example_app view
    path('example/', views.ExampleView.as_view()),

    # Path to the upload file view
    path('upload/', views.UploadFileView.as_view()),
    path('make_xml_message/', views.MakeXMLMessageView.as_view())
]
