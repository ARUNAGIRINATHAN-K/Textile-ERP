from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.users.urls')),
    path('api/procurement/', include('apps.procurement.urls')),
    path('api/inventory/', include('apps.inventory.urls')),
    path('api/ml/', include('apps.ml_api.urls')),
    # add other app url includes similarly
]
