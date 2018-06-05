#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL")
data = featureFormat(data_dict, features)


### your code below



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )


sal=[]
for k,v in data_dict.items():
	if(v["salary"]!='NaN'):
		sal.append(v["salary"])
	
print(max(sal))

for k,v in data_dict.items():
	salary=float(v.get("salary"))	
	if(salary==max(sal)):
		print(k)
		
		

# ~ for k,v in data_dict.items():
	# ~ salary=float(v.get("salary"))
	# ~ bonus=float(v.get("bonus"))
	# ~ if(salary>1000000 and bonus>=5000000):
		# ~ print(k)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
