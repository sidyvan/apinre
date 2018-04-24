from django.shortcuts import render

def index(request):
	return render(request, 'website/index.html')

def home(request):
	return render(request, 'website/home.html')
