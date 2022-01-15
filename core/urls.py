from django.contrib import admin
from django.urls import path, include

app_name = 'fryzjer'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fryzjer.urls'))
]

