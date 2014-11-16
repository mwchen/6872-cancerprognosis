from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from progApp.forms import LookUpForm

def index(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	return render_to_response('progApp/index.html', context)

# Doctors can look up information regarding 
def lookup(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	# Check to see if it is an HTTP POST.
	if request.method == 'POST':
		form = LookUpForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database.
			form.save(commit=True)

			# Now call the index() view.
			# The user will be shown the homepage.
			return results(request)
		else:
			# The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = LookUpForm()

	return render_to_response('progApp/lookup.html', {'form': form}, context)

# Response page after submitting the form.
def results(request):
	return HttpResponse("Thanks for submitting the form!")

# Doctors update the model with the information regarding the patient.
def updatePatient(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	return render_to_response('progApp/updatePatient.html', context)