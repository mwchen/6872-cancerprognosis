from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from progApp.forms import LookUpForm
from models import *
import json

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

#determines if the person can make the change to the database
def authorizeChange(request):	
	return True

#creates a cancer given a post request where type is the identifier of the cancer (breast)
	# and description is a description of the cancer
def createCancer(request):
	if authorizeChange(request):	
		try:
			new_cancer = Cancer()
			new_cancer.type = request.POST('type')
			new_cancer.description = request.POST('description')
			new_cancer.save()
			return HttpResponse("cancer created")
		except:
			return HttpResponse("bad request", status = 500)
	else:
		return HttpResonse("unauthorized change", status = 500)

# creates a treatment object given a post request where cancer is the type of the cancer
	# it treats, name is the name of the treatment, and description is a description
def createTreatment(request):
	if authorizeChange(request):
		try:
			treatment_cancer = Cancer.objects.get(type = request.POST('type'))
			new_treatment = Treatment()
			new_treatment.cancer = treatment_cancer
			new_treatement.name = request.POST('name')
			new_treatment.description = request.POST('description')
			new_treatment.save()
			return HttpResponse("treatment created")
		except:
			return HttpResponse("bad request", status = 500)
	else:
		return HttpResonse("unauthorized change", status = 500)

# creates a stage object given a post request where cancer is the type of the cancer
	#  name is the name of the stage(which is a number), and description is a description
def createStage(request):
	if authorizeChange(request):
		try:
			stage_cancer = Cancer.objects.get(type = request.POST('type'))
			new_stage = Stage()
			new_stage.cancer = stage_cancer
			new_stage.name = int(request.POST('name'))
			new_stage.description = request.POST('description')
			new_stage.save()
			return HttpResponse("stage created")
		except:
			return HttpResponse("bad request", status = 500)
	else:
		return HttpResponse("unauthorized change", status = 500)

### request POST: {'cancer': cancer type, 'treatment': treatment name or 'None', "gender" 0,1,2,  
	### "age": age, "stage": stage name or 'None'}
def logCancerData(request):
	if authorizeChange(Request):
		try:
			new_cancer_data = CancerData
			cancer = Cancer.objects.get(type = request.Post('cancer'))
			new_cancer_data.cancer = cancer
			if request.Post('treatment') != "None":
				treatment = Treatment.objects.get(name = request.Post('treatment'), cancer = cancer)
				new_cancer_data.treatment = treatment
			if request.POST('stage') != "None":
				stage = Stage.objects.get(name = request.Post('stage'), cancer = cancer)
				new_cancer_data.stage = stage
			new_cancer_data.gender = request.POST('gender')
			new_cancer_data.age = int(request.POST('age'))
			return HttpResponse("data logged")
		except:
			return HttpResponse("bad request", status = 500)
	else:
		return HttpResponse("unauthorized change", status = 500)

def getCancerProg(request):
	try:
		#cancer = Cancer.objects.get(type = request.GET('cancer'))

		response = {'cancer':'Breast Cancer', 'stage':1, 'gender':'Female', 'age':32,
			'1year':0.9, '2year':0.8, '3year':0.75, '4year':0.7, '5year':0.65, 'treatments':
			[{'name':'Lumpectomy:', 'cost':900, 'quality_of_life':2, '1year':0.95, '2year':0.85, '3year':0.80, '4year':0.75, '5year':0.70},
			 	{'name':'Mastectomy', 'cost':1200, 'quality_of_life':2, '1year':0.98, '2year':0.88, '3year':0.86, '4year':0.79, '5year':0.75}]}
		json_response = json.dumps(response)
		return HttpResponse(json_response, content_type='application/json')
	except:
		return HttpResponse("bad request", status = 500)
	

'''
	try:
		cancer = Cancer.objects.get(type = request.GET('cancer'))
		gender = request.GET('gender')
		age = reqest.GET('age')
		age_class = age/20
		if request.GET('stage') != 'None':
			stage = Stage.objects.get(name = request.Post('stage'), cancer = cancer)
		else:
			stage = None
		cancer_type_data = CancerData.objects.filter(cancer = cancer)
		related_data = {}
		for data in cancer_type_data
		related data = [x where ctd['age']/20 = age_class and 
	'''	

# Response page after submitting the form.
def results(request):
	context = RequestContext(request)
	# Make sure to check that something has been entered.
	
	return render_to_response('progApp/results.html', context)

# Doctors update the model with the information regarding the patient.
def updatePatient(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	return render_to_response('progApp/updatePatient.html', context)