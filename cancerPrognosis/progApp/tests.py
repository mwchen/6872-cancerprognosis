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
gu.name = 'Both'
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
t.cost = 10000
t.quality_of_life = 2
t.save()
t = Treatment()
t.cancer = Cancer.objects.get(type = 'Breast')
t.name = 'Breast - Mastectomy plus Radiation'
t.cost = 10000
t.quality_of_life = 1
t.save()

t = Treatment()
t.cancer = Cancer.objects.get(type = 'Stomach')
t.name = 'Stomach - Endoscopic resection'
t.cost = 20000
t.description = 'Resection refers to cutting out a tumor or part of an organ. In this operation, the cancer is removed through an endoscope (a long, flexible tube passed down the throat and into the stomach). This can be done only for some very early cancers where the chance of spread is very low.'
t.quality_of_life = 2
t.save()
t = Treatment()
t.cancer = Cancer.objects.get(type = 'Stomach')
t.name = 'Stomach - Total Gastrectomy'
t.cost = 15000
t.description = ' In this operation, the surgeon removes all of the stomach. The nearby lymph nodes are removed, and sometimes also the spleen and parts of the esophagus, intestines, pancreas, and other nearby organs. The end of the esophagus is then attached to part of the small intestine. People who have had a total gastrectomy can only eat a small amount of food at a time. Because of this, they must eat more often. This method is used if the cancer has spread throughout the stomach. It is also often used if the cancer is in the upper part of the stomach.'
t.quality_of_life = 0
t.save()


survive = [(835+2878+2135+1146+2030)/10, (931+2785+2122+1185+1828)/10, (873+2379+1994+1994+1130+1385)/10, (692+1785+1593+946+929)/10, (487+1270+1137+684+651)/10,(20393+47859+43465+25389+14343)/10]
putData('Breast', 50, 'Female', 'Breast - Unknown', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '1'
survive = [9024/10,8851/10,7761/10,5945/10,4229/10,151449/10]
putData('Breast', 60, 'Female', 'Breast - Unknown', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '2'

survive = [14279/10,11349/10,9331/10,7000/10,5303/10,117661/10]
putData('Breast', 70, 'Female', 'Breast - Unknown', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '3'

survive = [2473/10,4227/10,3779/10,2912/10,2046/10,70537/10]
putData('Breast', 30, 'Female', 'Breast - Unknown', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'



survive = [20,20,20,20,20,900]
putData('Breast', 30, 'Female', 'Breast - Lumpectomy plus Radiation', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'
survive = [20,20,20,20,20,900]
putData('Breast', 50, 'Female', 'Breast - Lumpectomy plus Radiation', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'
survive = [20,20,20,20,20,900]
putData('Breast', 60, 'Female', 'Breast - Lumpectomy plus Radiation', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'
survive = [20,20,20,20,20,900]
putData('Breast', 70, 'Female', 'Breast - Lumpectomy plus Radiation', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'
survive = [10,10,10,0,0,970]
putData('Breast', 30, 'Female', 'Breast - Mastectomy plus Radiation', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'
survive = [10,10,10,0,0,970]
putData('Breast', 50, 'Female', 'Breast - Mastectomy plus Radiation', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'
survive = [10,10,10,0,0,970]
putData('Breast', 60, 'Female', 'Breast - Mastectomy plus Radiation', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'
survive = [10,10,10,0,0,970]
putData('Breast', 70, 'Female', 'Breast - Mastectomy plus Radiation', survive, [[.30,.015],[.33,.015],[.32,.154],[.5,.75]])
print '4'


survive =[6704/10,2238/10,841/10,375/10,209/10,14758/10]
putData('Stomach', 50, 'Male', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '1'
survive = [15720/10,4893/10,1778/10,869/10,424/10,32479/10]
putData('Stomach', 60, 'Male', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '2'

survive = [30859/10,7744/10,2961/10,1279/10,722/10,55667/10]
putData('Stomach', 70, 'Male', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '3'

survive = [2476/10,829/10,300/10,127/10,63/10,5712/10]
putData('Stomach', 30, 'Male', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '4'


survive =[3216/10,1107/10,423/10,182/10,94/10,7713/10]
putData('Stomach', 50, 'Female', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '1'
survive = [6590/10,2059/10,732/10,356/10,198/10,14767/10]
putData('Stomach', 60, 'Female', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '2'

survive = [14866/10,3589/10,1383/10,649/10,365/10,28657/10]
putData('Stomach', 70, 'Female', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '3'

survive = [1896/10,694/10,224/10,89/10,65/10,4601/10]
putData('Stomach', 30, 'Female', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '4'
#data entered:  female breast 50

survive =[10/10,10/10,10/10,10/10,800/10,350/10]
putData('Stomach', 50, 'Female', 'Stomach - Endoscopic resection', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '1'
survive = [10/10,10/10,10/10,10/10,800/10,350/10]
putData('Stomach', 60, 'Female', 'Stomach - Endoscopic resection', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '2'

survive = [10/10,10/10,10/10,10/10,800/10,350/10]
putData('Stomach', 70, 'Female', 'Stomach - Endoscopic resection', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '3'

survive = [10/10,10/10,10/10,10/10,800/10,350/10]
putData('Stomach', 30, 'Female', 'Stomach - Endoscopic resection', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '4'


survive =[800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 50, 'Female', 'Stomach - Total Gastrectomy', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '1'

survive = [800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 60, 'Female', 'Stomach - Total Gastrectomy', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '2'

survive = [800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 70, 'Female', 'Stomach - Total Gastrectomy', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '3'

survive = [800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 30, 'Female', 'Stomach - Total Gastrectomy', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '4'

survive = [800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 30, 'Female', 'Stomach - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '4'
#data entered:  female breast 50

survive =[10/10,10/10,10/10,10/10,800/10,350/10]
putData('Stomach', 50, 'Male', 'Stomach - Endoscopic resection', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '1'
survive = [10/10,10/10,10/10,10/10,800/10,350/10]
putData('Stomach', 60, 'Male', 'Stomach - Endoscopic resection', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '2'

survive = [10/10,10/10,10/10,10/10,800/10,350/10]
putData('Stomach', 70, 'Male', 'Stomach - Endoscopic resection', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '3'

survive = [10/10,10/10,10/10,10/10,800/10,350/10]
putData('Stomach', 30, 'Male', 'Stomach - Endoscopic resection', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '4'


survive =[800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 50, 'Male', 'Stomach - Total Gastrectomy', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '1'
survive = [800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 60, 'Male', 'Stomach - Total Gastrectomy', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '2'

survive = [800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 70, 'Male', 'Stomach - Total Gastrectomy', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '3'

survive = [800/10,10/10,10/10,10/10,10/10,350/10]
putData('Stomach', 30, 'Male', 'Stomach - Total Gastrectomy', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '4'
#data entered:  female breast 50
#data entered:  female breast 50

survive =[6504/10,6987/10,5174/10,3842/10,2659/10,207837/10]
putData('Prostate', 60, 'Male', 'Prostate - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '1'
survive = [22002/10,20431/10,15580/10,11958/10,8894/10,386268/10]
putData('Prostate', 70, 'Male', 'Prostate - Unknown', survive, [[.13,.359],[.13,.359],[.29,.712],[.45,.958]])
print '2'
'''
