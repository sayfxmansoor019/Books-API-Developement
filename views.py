from django.shortcuts import render   #to return html only
from django.http import HttpResponse  #to return any type of data(json/xml/html etc)
from django.http import JsonResponse  #to return json only
from rest_framework.response import Response     # to return HTML View through rest

from .models import Books 
from .serializers import BookSerializer
from rest_framework.decorators import api_view   #importing decorator for request type handling
from rest_framework.response import Response     # to return HTML View
from rest_framework import status
import requests

# Create your views here.
@api_view(['GET', 'POST'])  #decorator to make the below function accept get, post request
def book_list(request):
    #get all books
    #serialize
    #return json

    if request.method == 'GET':
        b = Books.objects.all()
        bserializer = BookSerializer(b, many=True)
        # return JsonResponse(bserializer.data, safe=False)  #direct json
        # return JsonResponse({ 'books':bserializer.data})  #safe = false req when not using dict
        # return HttpResponse(bserializer.data,content_type = 'application/json' )  #using httpresponse and then json type
        return Response(bserializer.data)   #to return html view through rest

    elif request.method == 'POST':
        bserializer = BookSerializer(data = request.data)  #create object
        if bserializer.is_valid():  #check if data is valis
            bserializer.save()      #save
            return Response(bserializer.data, status = status.HTTP_201_CREATED) #return response
        

@api_view(['GET', 'PUT', 'DELETE'])
def book_id(request, id):
    try:
        b = Books.objects.get(pk = id)
    except Books.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': #send data
        bserializer = BookSerializer(b)
        return Response(bserializer.data)
    elif request.method == 'PUT':  #edit data
        bserializer = BookSerializer(b, data=request.data)
        if bserializer.is_valid():
            bserializer.save()
            return Response(bserializer.data)
        return Response(bserializer.error, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        b.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)