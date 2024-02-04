from django.urls import path

from . import views

urlpatterns = [
    path('', views.guidelines_view, name='guidelines'),
    path('<str:guide>', views.guide_view, name='guide'),    
    # path('documents/', views.documents_view, name='documents'),
    path('documents/<int:documentId>', views.document_view, name='document'),    
]
