from django.test import TestCase

# Create your tests here.
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
all_cancers = ['Lip', 'Skin Melanoma', 'Tounge', 'Breast', 'Oral Cavity', 'Cervix Uteri', 'Salivary Gland', 'Corpus Uteri',
	'Oropharynx', 'Ovary', 'Nasopharynx', 'Vagina and vulva', 'Hypopharynx', 'Prostate', 'Head and Neck', 'Testis', 
	'Esophagus', 'Penis', 'Stomach', 'Urinary Bladder', 'Small Intestine', 'Kidney', 'Colon Rectum', 'Brain', 'Colon', 'Thyroid',
	'Rectum', 'Plasma cell', 'Liver', "Hodgkin's lymphoma", 'Gallbladder', "Non Hodgkin lymphoma", 'Pancrease', 'SBLL/CLL', 
	'Nasal cavaties and sinuses', 'LL/ALL', 'Larynx', 'AML', 'Lung', 'MPN', 'Pleura', 'CML', 'Bones and cartilages', 'MDS']
putCancers(all_cancers)
t = Treatment()
t.cancer = Cancer.objects.get(type = 'Breast')
t.name = 'Breast - Lumpectomy plus Radiation'
t.cost = 20000
t.quality_of_life = 2
t.save()
t = Treatment()
t.cancer = Cancer.objects.get(type = 'Breast')
t.name = 'Breast - Mastectomy plus Radiation'
t.cost = 25000
t.quality_of_life = 1
t.save()


survive = [(835+2878+2135+1146+2030)/10, (931+2785+2122+1185+1828)/10, (873+2379+1994+1994+1130+1385)/10, (692+1785+1593+946+929)/10, (487+1270+1137+684+651)/10,(20393+47859+43465+25389+14343)/10]
putData('Breast', 50, 'Female', 'Breast - Unknown', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '1'
survive = [9024/10,8851/10,7761/10,5945/10,4229/10,151449/10]
putData('Breast', 60, 'Female', 'Breast - Unknown', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '2'

survive = [14279/10,11349/10,9331/10,7000/10,5303/10,117661/10]
putData('Breast', 70, 'Female', 'Breast - Unknown', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '3'

survive = [2473/10,4227/10,3779/10,2912/10,2046/10,70537/10]
putData('Breast', 30, 'Female', 'Breast - Unknown', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'



survive = [20,20,20,20,20,1000]
putData('Breast', 30, 'Female', 'Breast - Lumpectomy plus Radiation', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'
survive = [20,20,20,20,20,1000]
putData('Breast', 50, 'Female', 'Breast - Lumpectomy plus Radiation', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'
survive = [20,20,20,20,20,1000]
putData('Breast', 60, 'Female', 'Breast - Lumpectomy plus Radiation', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'
survive = [20,20,20,20,20,1000]
putData('Breast', 70, 'Female', 'Breast - Lumpectomy plus Radiation', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'
survive = [10,10,10,0,0,1000]
putData('Breast', 30, 'Female', 'Breast - Mastectomy plus Radiation', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'
survive = [10,10,10,0,0,1000]
putData('Breast', 50, 'Female', 'Breast - Mastectomy plus Radiation', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'
survive = [10,10,10,0,0,1000]
putData('Breast', 60, 'Female', 'Breast - Mastectomy plus Radiation', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'
survive = [10,10,10,0,0,1000]
putData('Breast', 70, 'Female', 'Breast - Mastectomy plus Radiation', survive, [[.30,.0075],[.33,.0075],[.32,.154],[.5,.75]])
print '4'


#data entered:  female breast 50
