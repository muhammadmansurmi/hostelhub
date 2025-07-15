from django.urls import path
from .views import submit_request, view_requests

urlpatterns = [
    path('', submit_request, name='submit'),         # http://127.0.0.1:8000/submit/
    path('all/', view_requests, name='view_requests')  # http://127.0.0.1:8000/submit/all/
]
