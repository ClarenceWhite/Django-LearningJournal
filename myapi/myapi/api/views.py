from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from api.models import People

def index(request):
    response = json.dumps([{'Index': 'This is the index page'}])
    return HttpResponse(response, content_type='text/json')

def get_people(request, people_name):
    if request.method == 'GET':
        try:
            people = People.objects.get(name=people_name)
            response = json.dumps([{'People': people.name, 'Sex': people.sex}])
        except:
            response = json.dumps([{'Error': 'No such a person'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_people(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        people_name = payload['people_name']
        people_sex = payload['people_sex']
        people = People(name=people_name, sex=people_sex)
        try:
            people.save()
            response = json.dumps([{'Success': 'People added successfully!'}])
        except:
            response = json.dumps([{'Error': 'failed to add people'}])

    return HttpResponse(response, content_type='text/json')
