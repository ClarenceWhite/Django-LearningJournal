from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from mysql_api.models import CurrentWeather
from mysql_api.serializers import current_weather_serializer
# Create your views here.

@csrf_exempt
def current_weather_api(request):
    if request.method == 'GET':
        current_weather_data = CurrentWeather.objects.all()
        current_weather_data_serializer = current_weather_serializer(current_weather_data, many=True)
        return JsonResponse(current_weather_data_serializer.data, safe=False)