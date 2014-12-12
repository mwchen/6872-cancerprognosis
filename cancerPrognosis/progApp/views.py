from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
import json
from models import *
import datetime
from progApp.forms import LookUpForm, UpdateDataForm
from reportlab.pdfgen import canvas
from django.views.static import serve
import reportlab


def index(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	return render_to_response('progApp/index.html', context)

# Doctors can look up information regarding a patient.
@csrf_exempt
def lookup(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	# Check to see if it is an HTTP POST.
	if request.method == 'POST':
		#form = LookUpForm(request.POST)

		# Have we been provided with a valid form?
		# Would normally check this but this doesn't make sense because we are prepopulating.
		# #if form.is_valid():
		# 	## Save the new category to the database.
		# 	#form.save(commit=True)
		# 	getCancerProg(request)

		# 	# Now call the index() view.
		# 	# The user will be shown the homepage.
		# 	return results(request)
		# else:
		# 	# The supplied form contained errors - just print them to the terminal.
		# 	print form.errors
		#json_data = getCancerProg(request)
		return getCancerProg(request)
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
	if authorizeChange(request):
		try:
			new_cancer_data = CancerData()
			cancer = Cancer.objects.get(id = request.POST['cancer'])
			new_cancer_data.cancer = cancer
			if request.POST['treatment'] != "None":
				treatment = Treatment.objects.get(id = request.POST['treatment'])
				new_cancer_data.treatment = treatment
			if request.POST['stage'] != "None":
				new_cancer_data.stage = request.POST['stage']
			new_cancer_data.gender = Gender.objects.get(id = request.POST['gender'])
			new_cancer_data.age = groupAge(int(request.POST['age']))
			new_cancer_data.save()
			fast = quickCancerLookup.objects.filter(cancer = cancer)
			for f in fast:
				f.delete()

			return HttpResponse("data logged", status = 200)
		except:
			return HttpResponse("bad request", status = 500)
	else:
		return HttpResponse("unauthorized change", status = 500)
	
def logClinicalTrial(request):
	if True:
		new_ct = ClinicalTrial()
		cancer = Cancer.objects.get(id = request.POST['cancer'])
		new_ct.cancer = cancer
		new_ct.gender = Gender.objects.get(id = request.POST['gender'])
		new_ct.age_hi = int(request.POST['age_hi'])
		new_ct.age_low = int(request.POST['age_low'])
		start = datetime.datetime.strptime(request.POST['start_date'], '%d-%m-%Y')
		new_ct.start_date = start
		end = datetime.datetime.strptime(request.POST['end_date'], '%d-%m-%Y')
		new_ct.end_date = end
		new_ct.location = request.POST['location']
		new_ct.name = request.POST['name']
		new_ct.contact = request.POST['contact']
	else:
		return HttpResponse("data logged", status = 200)
		
def getClinicalTrial(request):
	if True:
		cancer = Cancer.objects.get(id = request.POST['cancer'])
		stage = request.POST['stage']
		gender = Gender.objects.get(id = request.POST['gender'])
		age = int(request.POST['age'])
		ct_list = ClincialTrial.objects.filter(age_hi <= age, age_low >= age, gender = gender, stage = stage, cancer = cancer)
		response = [{'name': ct.name, 'contact':ct.contact, 'location':	ct.location, 'end_date': ct.end_date, 
			'start_date': ct.start_date} for ct in ct_list]
		json_response = json.dumps(response)
		return HttpResponse(json_response, type = 'javascript/application')
	else:
		return HttpResponse('bad request', 500)
		

def convertYears(x,dic):
	for v in dic.keys():
		if x >= v:
			dic[v] += 1
def groupAge(x):
	if x < 20:
		return 10
	elif x < 40:
		return 30
	elif x < 60:
		return 50
	elif x < 80:
		return 70
	elif x< 100:
		return 90
	elif x< 120:
		return 110

@csrf_exempt	

def getCancerProg(request):
	try:
		cancer = Cancer.objects.get(id = request.POST['cancer'])
		if 'age' in request.POST:
			pre_age = request.POST['age']
		else:
			pre_age = None
		pre_stage = str(request.POST['stage'])
		gender = Gender.objects.get(id = request.POST['gender'])
		stage = Stage.objects.get(cancer = cancer, name = pre_stage)
		if pre_age != None:	
			age = groupAge(int(pre_age))
		else:
			age = -1
			
		try:
			fast = quickCancerLookup.objects.get(name = cancer.type +'-'+str(age)+'-'+gender.name + '-' + str(stage.name))
			return HttpResponse(fast.data, content_type='application/json')
		except:
			cancerdata = CancerData.objects.filter(cancer = cancer)
			print len(cancerdata)
			if len(cancerdata) < 100:
				json_response = json.dumps({'cancer':cancer.type, 'stage':stage.name, 'gender':gender.name, 'age':age,
				'1year':1, '2year':1, '3year':1, '4year':1, '5year':0.1, 'treatments': 
					[{'name':'Unkown:', 'cost':100, 'quality_of_life':2, '1year':1, '2year':1, '3year':1, '4year':1, '5year':1}]})
				return HttpResponse(json_response, content_type='application/json')
			treatments = Treatment.objects.filter(cancer = cancer)
			counting_dic = {'total': {0:.0001, 1:.0001, 2:.0001, 3:.0001, 4:.0001, 5:.0001}}
			for t in treatments:
				counting_dic[t.name] = {1:.0001, 2:.0001, 3:.0001, 4:.0001, 5:.0001, 0:.0001}
		
			for cd in cancerdata:
				if age == -1 or (cd.age <= (age + 10) and cd.age >= (age -10)):
					if  gender.name == 'Both' or cd.gender == gender:
						if cd.stage == stage.name:
							convertYears(cd.years_lived, counting_dic['total'])
							convertYears(cd.years_lived, counting_dic[cd.treatment.name])
			response = {'cancer':cancer.type, 'stage': stage.name, 'gender': gender.name, 'age': pre_age}
			response['1year'] = round((counting_dic['total'][1])/float(counting_dic['total'][0]),5)
			response['2year'] = round((counting_dic['total'][2])/float(counting_dic['total'][0]),5)
			response['3year'] = round((counting_dic['total'][3])/float(counting_dic['total'][0]),5)
			response['4year'] = round((counting_dic['total'][4])/float(counting_dic['total'][0]),5)
			response['5year'] = round((counting_dic['total'][5])/float(counting_dic['total'][0]),5)
			response['treatments'] = []
			for t in treatments:
				if t.name != cancer.type + ' - Unknown':
					new_treatment_dic = {}
					new_treatment_dic['name'] = t.name
					new_treatment_dic['cost'] = t.cost
					new_treatment_dic['quality_of_life'] = t.quality_of_life
					new_treatment_dic['1year'] = round((counting_dic[t.name][1])/float(counting_dic[t.name][0]),5)
					new_treatment_dic['2year'] = round((counting_dic[t.name][2])/float(counting_dic[t.name][0]),5)
					new_treatment_dic['3year'] = round((counting_dic[t.name][3])/float(counting_dic[t.name][0]),5)
					new_treatment_dic['4year'] = round((counting_dic[t.name][4])/float(counting_dic[t.name][0]),5)
					new_treatment_dic['5year'] = round((counting_dic[t.name][5])/float(counting_dic[t.name][0]),5)
					response['treatments'].append(new_treatment_dic)
		
			json_response = json.dumps(response)
			try:
				fast = quickCancerLookup.objects.filter(name = cancer.type +'-'+str(age)+'-'+gender.name+'-' + str(stage.name))
				fast.delete()
			except:
				pass
					
			fast = quickCancerLookup()
			fast.name = cancer.type +'-'+str(age)+'-'+gender.name + '-' + str(stage.name)
			fast.data = json_response
			fast.cancer = cancer
			fast.save()
			'''
			response = {'cancer':'Breast Cancer', 'stage':1, 'gender':'Female', 'age':32,
				'1year':0.9, '2year':0.8, '3year':0.75, '4year':0.7, '5year':0.65, 'treatments':
				[{'name':'Lumpectomy:', 'cost':900, 'quality_of_life':2, '1year':0.95, '2year':0.85, '3year':0.80, '4year':0.75, '5year':0.70},
			 		{'name':'Mastectomy', 'cost':1200, 'quality_of_life':2, '1year':0.98, '2year':0.88, '3year':0.86, '4year':0.79, '5year':0.75}]}
			json_response = json.dumps(response)
			'''
			return HttpResponse(json_response, content_type='application/json')
	except Exception as e:
		return HttpResponse("bad request %s (%s)" % (e.message, type(e)), status = 500)

def getDetails(request):
	try:
		cancer = Cancer.objects.get(type = request.GET['cancer'])
		treatment_list = Treatment.objects.get(cancer = cancer)
		stage = Stage.objects.get(cancer = cancer, name = request.GET['stage'])
		treatment_descriptions = {}
		for t in treatment_list:
			treatment_descriptions[t.name] = t.description
		response = {'cancer_description':cancer.description, 'stage_description':stage.description, 
			'treatments':treatment_list}
		json_response = json.dumps(response)
		return HttpResponse(json_response, content_type = 'application/json')
	except:
		return HttpResponse("bad request", status = 500)

# Doctors update the model with the information regarding the patient.
def updatePatient(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	# Check to see if it is an HTTP POST.
	if request.method == 'POST':
		return logCancerData(request)
	else:
		# If the request was not a POST, display the form to enter details.
		form = UpdateDataForm()
	return render_to_response('progApp/updatePatient.html', {'form': form}, context)

	

def putCancers(cancers):
	for c in cancers:
		nc = Cancer()
		nc.type = c
		nc.description = 'A cancer of the '+ c
		nc.save()
		t = Treatment()
		t.cancer = nc
		t.name = c + " - Unknown"
		t.description = 'Unknown Treatment'
		t.quality_of_life = 1
		t.cost = 0
		t.save()
		s = Stage()
		s.name = '1'
		s.description = 'The first stage of '+c+' cancer. The cancer is local to the region.'
		s.cancer = nc
		s.save()
		s = Stage()
		s.name = '2'
		s.description = 'The second stage of '+c+' cancer.  The cancer is local to the region.'
		s.cancer = nc
		s.save()
		s = Stage()
		s.name = '3'
		s.description = 'The third stage of '+c+' cancer. The cancer has spread to areas near the initial region.'
		s.cancer = nc
		s.save()
		s = Stage()
		s.name = '4'
		s.description = 'The fourth stage of '+c+' cancer. The cancer has spread to other areas in the body'
		s.cancer = nc
		s.save()

class Req():
	POST = {}
def putData(cancer, age, gender, treat, survived,stage_probs):
	for st in range(1,5):
		cancer = Cancer.objects.get(type = cancer)
		treatment = Treatment.objects.get(cancer = cancer, name = treat)
		stage  = Stage.objects.get(cancer = cancer, name = st)
		gender = Gender.objects.get(name = gender)
		x = 0
		for s in range(len(survived)):
			if s <5:
				num = int(survived[s]*stage_probs[st-1][0]*stage_probs[st-1][1]+1)
			else:
				num = int(survived[s]*stage_probs[st-1][0]*(1-stage_probs[st-1][1])+1)
				
			for c in range(num):
				x += 1
				cd = CancerData()
				cd.cancer = cancer
				cd.treatment = treatment
				cd.stage = int(stage.name)
				cd.gender = gender
				cd.age = groupAge(age)
				cd.years_lived = s
				cd.save()
				
class Request():
	POST = {}

from reportlab.lib.colors import Color, blue, red, white
from reportlab.graphics.charts.legends import Legend, TotalAnnotator  
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin  
from reportlab.lib.validators import Auto  
from reportlab.graphics.charts.lineplots import AreaLinePlot  
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor


def generateGraph(data, min, max):
	dl = Drawing(400, 200)
	lp = AreaLinePlot()
	lp.data=data
	lp.width, lp.height = 400, 200
	lp.xValueAxis.valueMin = 1
	lp.xValueAxis.valueMax =5
	lp.xValueAxis.valueSteps = [1,2,3,4,5]
	lp.yValueAxis.valueMin = min
	lp.yValueAxis.valueMax =max
	lp.strokeColor=reportlab.lib.colors.HexColor('#193441')
	lp.fillColor=reportlab.lib.colors.HexColor('#fcfff5')
	lp.lines[0].strokeColor =reportlab.lib.colors.HexColor('#193441')
	lp.reversePlotOrder = False
	lp.joinedLines=1
	dl.add(lp)
	return dl
def post_text(text,canvas,x,y):
	words = text.split(' ')
	while len(words) > 0:
		line = ''
		while len(line) < 85:
			if len(line) == 0:
				line = words.pop(0)
			else:
				line = line + ' ' + words.pop(0)
			if len(words) == 0:
				break
		canvas.drawString(x,y,line)
		y += -17
	return y
@csrf_exempt	
def pdf(request):
	happy = {0:'Difficult', 1:'Moderate Difficulties', 2: 'No Change In Life-Style'}
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="PatientView.pdf"'
	p = canvas.Canvas(response)
	x = 20
	y = 780
	r = Request()
	r.POST['cancer'] = request.GET['cancer']
	r.POST['stage'] = request.GET['stage']
	r.POST['age'] = request.GET['age']
	r.POST['gender'] = request.GET['gender']
	ans = getCancerProg(r)
	
	for a in ans:
		data = json.loads(a)
	p.setFillColor(HexColor(0x193441))
	cancer = Cancer.objects.get(type = data['cancer'])
	stage  = Stage.objects.get(cancer = cancer, name = str(data['stage']))
	p.setFont("Helvetica-Bold", 38)
	p.drawString(x-6,y,'Cancer Prognosis Patient Sheet')
	y = y -40
	p.setFont("Helvetica-Bold",20)
	p.drawString(x-5,y,'Patient Diagnosis')
	y += -20
	p.setFont("Helvetica-Bold",14)
	p.setFillColor(HexColor(0x193441))
	p.drawString(x-5, y, data['gender'])
	y += -20
	p.drawString(x-5, y, str(data['age']) + ' Years Old')
	y += -20
	p.drawString(x-5,y,data['cancer'] + ' Cancer')
	p.setFillColor(HexColor(0x000000))

	y = y - 20
	p.setFont("Helvetica",14)
	y = post_text(cancer.description,p,x,y)
	p.setFont("Helvetica-Bold",14)
	p.setFillColor(HexColor(0x193441))
	p.drawString(x-5, y , 'Stage '+str(data['stage']))
	p.setFillColor(HexColor(0x000000))
	y += -20
	p.setFont("Helvetica",14)
	y = post_text(stage.description,p,x,y)
	p.setFont("Helvetica-Bold",14)
	
	y = y - 30
	p.setFont("Helvetica-Bold",20)
	p.drawString(x-5,y,'Possible Treatments')
	y += -20
	p.setFont("Helvetica",14)
	count = 1
	for t in data['treatments']:
		if y < 200:
			p.showPage()
			y = 780
		treat = Treatment.objects.get(cancer = cancer, name = t['name'])
		p.setFont("Helvetica-Bold",14)
		p.setFillColor(HexColor(0x193441))

		p.drawString(x-5,y,'Treatment ' + str(count)+':' )
		y = y - 20
		p.drawString(x-5,y,t['name'])
		y = y - 20
		p.setFillColor(HexColor(0x000000))
		p.setFont("Helvetica",14)
		y = post_text(treat.description, p, x, y)
		p.setFillColor(HexColor(0x193441))
		p.setFont("Helvetica-Bold",14)
		p.drawString(x-5,y,'Average Cost: $' + str(t['cost']) )
		y = y - 20
		p.drawString(x-5,y,'Quality of Life: ' + happy[t['quality_of_life']] )
		y = y - 25
		p.drawString(x+ 180,y,'Probability of Survival')
		y = y -217
		if y < 150:
			p.showPage()
			y = 780
			y = y - 217
		graph = generateGraph([(1, t['1year']), (2, t['2year']), (3,t['3year']), (4, t['4year']), (5, t['5year'])], min([t['5year'],t['1year'],t['2year'],t['3year'],t['4year']]), max([t['5year'],t['1year'],t['2year'],t['3year'],t['4year']]))
		renderPDF.draw(graph,p, x+20, y)
		p.setFillColor(HexColor(0x000000))
		y += -20
		p.setFont("Helvetica",12)
		p.drawString(x+ 225,y,'Years')
		y = y - 50
		count += 1
		
		

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response
