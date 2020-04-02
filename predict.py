import random
from load import *

#load data
diseases=get_disease()
dictionary=get_dis_symp()
symptoms=get_symptoms()

done=[]

print('now I am going to ask for symptoms')

#start asking questions
while True:
    #choose random symptom
    randomsymp=random.choice(symptoms)
    print(str(randomsymp)+'?')
    yorn=input('type y for yes n for no:')
    print('\n')

    done.append(randomsymp)
    
    #if symptom is present then remove diseases from dictionary that dont have that symptom
    if yorn=='y':
        des=[key for key,value in dictionary.items() if randomsymp not in value]
        for d in des:
            dictionary.pop(d,None)
            diseases.remove(d)
    
    #else remove diseases from dictionary that have that symptom
    else:
        dis=[key for key,value in dictionary.items() if randomsymp in value]
        for t in dis:
            dictionary.pop(t,None)
            diseases.remove(t)

    #keep narrowing down the list of diseases until there are 4 or less diseases left        
    symptoms=[x for key,value in dictionary.items() for x in value if x not in done]
    if len(diseases)<4:
        print('you should get checked for'+str(diseases))
        break
                

    
