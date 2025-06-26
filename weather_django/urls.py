from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('weather_app.urls')),  # ✅ connect your app
    path('admin/', admin.site.urls),
]
