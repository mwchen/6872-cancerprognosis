from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	return render_to_response('progApp/index.html', context)

def lookup(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	return render_to_response('progApp/lookup.html', context)

def updatePatient(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	return render_to_response('progApp/updatePatient.html', context)