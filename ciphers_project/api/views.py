from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def greetings(request):
    result = {'message': "welcome to ciphers service!"}
    return JsonResponse(result)