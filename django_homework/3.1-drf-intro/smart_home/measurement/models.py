from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание датчика')

    def __str__(self):
        return self.name

class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время измерения')
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Датчик', related_name='measurement')
    image = models.ImageField(null=True, blank=True, verbose_name='Снимки')

    def __str__(self):
        return f'{self.id_sensor.name} - {self.temperature}'
