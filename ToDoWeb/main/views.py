from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(reponse):
	return render(reponse, "main/home.html")
