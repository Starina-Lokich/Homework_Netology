from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, AllSensorsSerializer, MeasurementSerializer
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
class AllSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = AllSensorsSerializer
    

class OneSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateSerializer(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
        