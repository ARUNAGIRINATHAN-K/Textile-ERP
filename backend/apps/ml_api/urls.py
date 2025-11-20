from django.urls import path
from .views import predict_demand

urlpatterns = [
    path('predict/demand/', predict_demand, name='predict-demand'),
]
