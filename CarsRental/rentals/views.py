from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home(request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.")



