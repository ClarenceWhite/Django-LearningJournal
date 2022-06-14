from django.urls import URLPattern, path
from . import views
 
urlpatterns = [
    path('hello/', views.hello)
 ]