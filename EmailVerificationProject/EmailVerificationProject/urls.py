from django.contrib import admin
from django.urls import path, include  # Inclua o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Adicione esta linha
]
