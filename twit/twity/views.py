from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
	return render(request,'home.html');
def add(request):
	print(request.GET)
	print(request)
	return render(request,'s3.html');