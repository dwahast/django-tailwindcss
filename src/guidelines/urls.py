from django.urls import path

from . import views

urlpatterns = [
    path('documents/', views.documents_view, name='documents'),
    path('documents/<int:documentId>', views.document_view, name='document'),    
]
