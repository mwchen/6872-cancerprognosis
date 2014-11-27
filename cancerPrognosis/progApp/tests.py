from django.test import TestCase

# Create your tests here.
'''
from views import *
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
survive = [3570+162+156+134+87,162,156,134,87,3570]
putCancers(all_cancers)

putData('Breast', 50, 'Female', 'Unknown', '1', survive)
'''

class Req():
	POST = {}
g = Req()
g.POST = {'cancer':'Breast', 'stage':1, 'gender':'Female', 'age':45}
print getCancerProg(g)
print getCancerProg(g)