from django.shortcuts import render

# Create your views here.

def home(request):
	template = "landing\page.html"
	context = {}

	return render(request,template,context)
