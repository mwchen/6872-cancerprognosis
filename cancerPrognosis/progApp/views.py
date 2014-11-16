from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	return render_to_response('progApp/index.html', context)

def doctorView(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)
	return HttpResponse("REACHED")
	#return render_to_response('doctorView.html', context)