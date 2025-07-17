from django.urls import path
from .views import submit_request, view_requests

urlpatterns = [
    path('', submit_request, name='submit'),
    path('all/', view_requests, name='view_requests'),
]
