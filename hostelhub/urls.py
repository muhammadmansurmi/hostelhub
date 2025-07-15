from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', include('maintenance.urls')),  # This must match what you're visiting
]
