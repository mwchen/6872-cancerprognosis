from django.test import TestCase

# Create your tests here.
from views import *
'''
gm = Gender()
gm.name = 'Male'
gm.save()
gf = Gender()
gf.name = 'Female'
gf.save()
gu = Gender()
gu.name = 'Unknown'
gu.save()
breast = Cancer()
breast.type = 'Breast Cancer'
breast.description = 'cancer of the breast'
breast.save()
t = Treatment()
t.cancer = breast
t.name = 'No Treatment'
t.description = 'No treatment'
t.quality_of_life = 0
t.cost = 0
t.save()

tt = Treatment()
tt.cancer = breast
tt.name = 'Mysectomy'
tt.description = 'removal of breast'
tt.quality_of_life = 3
tt.cost = 10000
tt.save()

s = Stage()
s.cancer = breast
s.name = '1'
s.description = 'first stage'
s.save()

cd = CancerData()
cd.cancer = breast
cd.treatment =tt
cd.stage = s
cd.gender = gf
cd.age = 20
cd.years_lived = 5
cd.save()

cd = CancerData()
cd.cancer = breast
cd.treatment =t
cd.stage = s
cd.gender = gf
cd.age = 20
cd.years_lived = 2
cd.save()

cd = CancerData()
cd.cancer = breast
cd.treatment =t
cd.stage = s
cd.gender = gf
cd.age = 20
cd.years_lived = 4
cd.save()
all_cancers = ['Lip', 'Skin Melanoma', 'Tounge', 'Breast', 'Oral Cavity', 'Cervix Uteri', 'Salivary Gland', 'Corpus Uteri',
	'Oropharynx', 'Ovary', 'Nasopharynx', 'Vagina and vulva', 'Hypopharynx', 'Prostate', 'Head and Neck', 'Testis', 
	'Esophagus', 'Penis', 'Stomach', 'Urinary Bladder', 'Small Intestine', 'Kidney', 'Colon Rectum', 'Brian', 'Colon', 'Thyroid',
	'Rectum', 'Plasma cell', 'Liver', "Hodgkin's lymphoma", 'Gallbladder', "Non Hodgkin lymphoma", 'Pnacrease', 'SBLL/CLL', 
	'Nasal cavaties and sinuses', 'LL/ALL', 'Larynx', 'AML', 'Lung', 'MPN', 'Pleura', 'CML', 'Bones and cartilages', 'MDS']
putCancers(all_cancers)

survive = [20393,835,931,873,692,487]
putData('Breast', 50, 'Female', 'Unknown', '1', survive)
survive = [47859,2878, 2785, 2379, 1785, 1270]
putData('Breast', 50, 'Female', 'Unknown', '1', survive)
survive = [43465,2135,2122,1994,1593,1137]
putData('Breast', 50, 'Female', 'Unknown', '1', survive)
survive = [25389,1146, 1185, 1130, 946, 684]
putData('Breast', 50, 'Female', 'Unknown', '1', survive)
survive = [14343,2030, 1828, 1385, 929, 651]
putData('Breast', 50, 'Female', 'Unknown', '1', survive)



#data entered:  female breast 50

''' 

class Req():
	POST = {}
g = Req()
g.POST = {'cancer':'Breast', 'stage':1, 'gender':'Female', 'age':45}
print getCancerProg(g)
print getCancerProg(g)
