from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from .forms import SurveyForm
import custom_apis
from django.contrib import messages
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def survey(request):
	form = SurveyForm(request.POST or None)
	success = False
	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=True)
			instance.save()
			form = SurveyForm()
			success = True
			messages.add_message(request, messages.SUCCESS, 'Thanks. Your details has been saved.')
	context = {"form":form,"title":"Real-Estate Survey"}
	return render(request, "survey.html", context)



def getArea(request):

	return JsonResponse(custom_apis.getAPIAreaByCity('Bangalore', 'Sar'))

def getProperty(request):
	return JsonResponse(custom_apis.getAPIPropertyByArea('Bangalore','27694'))

def getApartment(request):
	city_name = request.GET.get('city_name')
	area_name = request.GET.get('area_name')
	print city_name, area_name
	url = "https://www.commonfloor.com/autosuggest.php?c="+ city_name +"&item=locationbuilderproject&str="+area_name+"&res_type=json"
	import requests, json
	return JsonResponse(json.loads(requests.get(url).text))