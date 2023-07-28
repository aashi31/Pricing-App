
from django.contrib import admin
from django.urls import path, include
from pricing_app.views import homepage  # Import the homepage view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pricing/', include('pricing_app.urls')),  # Assuming you have separate URL patterns for pricing_app
    path('', homepage, name='homepage'),  # Add the URL pattern for the homepage
]

