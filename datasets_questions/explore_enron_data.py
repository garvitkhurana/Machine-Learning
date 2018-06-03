#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))



# ~ print(len(enron_data))
# ~ t=(enron_data.values()[0])
# ~ print(len(t))





# ~ c=0
# ~ for k,v in enron_data.items():
	# ~ if(enron_data[k]['poi']==1):
		# ~ c=(c+1)
# ~ print(c)





# ~ file = open("../final_project/poi_names.txt","r")
# ~ m=file.readlines()
# ~ print(len(m))




# ~ print enron_data["Colwell Wesley".upper()]
# ~ print enron_data["SKILLING JEFFREY K"]



# ~ money=0
# ~ people = ("SKILLING JEFFREY K", "LAY KENNETH L","FASTOW ANDREW S") 
# ~ who = ""

# ~ for i in people:
	# ~ if money<enron_data[i]["total_payments"]:
		# ~ money = enron_data[i]["total_payments"]
		# ~ who = i
	
# ~ print(money,who)



# ~ sal,email=0,0		
		
# ~ for i in enron_data.values():
	# ~ if(i["salary"]!="NaN"):
		# ~ sal+=1
	# ~ if(i["email_address"]!="NaN"):
		# ~ email+=1
		
# ~ print(sal,email)




# ~ tot_pay=0


# ~ for i in enron_data.values():
	# ~ if(i["total_payments"]=="NaN"):
		# ~ tot_pay+=1
		
# ~ print(tot_pay / float(len(enron_data)))


# ~ c=0
# ~ for i in enron_data.values():
	# ~ if(i['poi']==1 and i["total_payments"]=="NaN"):
		# ~ c+=1
# ~ print c


# ~ c=0
# ~ for i in enron_data.values():
	# ~ if(i["total_payments"]!="NaN"):
		# ~ c+=1
# ~ print c
