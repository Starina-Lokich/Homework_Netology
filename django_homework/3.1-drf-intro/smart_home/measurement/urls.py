from django.urls import path
from measurement.views import AllSensorView, OneSensorView, MeasurementCreateSerializer

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', AllSensorView.as_view()),
    path('sensors/<pk>/', OneSensorView.as_view()),
    path('measurements/', MeasurementCreateSerializer.as_view()),
]
