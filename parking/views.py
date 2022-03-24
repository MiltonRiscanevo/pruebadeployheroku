from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializer import CarSerializer
from .models import Car
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt

def car_List (request):
    
    if request.method =="GET":
        cars= Car.objects.all()
        serializer = CarSerializer(cars, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer = CarSerializer(
            data = data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
@csrf_exempt
def car_get_info(request,pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return HttpResponse(status=404)
    if request.method =="GET":
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data, safe = False)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CarSerializer(car, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        car.delete()
        return HttpResponse(status = 204)



