from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MYAPP.urls')),
]

handler404 = 'MYAPP.views.error_404_view'