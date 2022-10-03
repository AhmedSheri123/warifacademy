from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("choose2", views.choose2, name="choose2"),
    path('questions', views.question, name="questions"),
    path('viewPoints', views.viewPoints, name="viewPoints"),
    path('ExportPdf', views.ExportPdf, name="ExportPdf"),
    path('ExportPdfAllFigures', views.ExportPdfAllFigures, name="ExportPdfAllFigures"),
]
