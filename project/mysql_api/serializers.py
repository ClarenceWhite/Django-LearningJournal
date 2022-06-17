from rest_framework import serializers
from mysql_api.models import CurrentWeather

class current_weather_serializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentWeather
        fields = ('date_time', 'temp', 'main', 'description', 'icon')