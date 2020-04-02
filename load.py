import pickle

#load all diseases data
def get_disease():
    f=open('diseases.pkl','rb')
    diseases=pickle.load(f)
    f.close()
    return(diseases)


def get_symptoms():
    f=open('symptoms.pkl','rb')
    symptoms=pickle.load(f)
    f.close()
    return(symptoms)


def get_dis_symp():    
    f=open('dis-symp-dict.pkl','rb')
    dictionary=pickle.load(f)
    f.close()
    return(dictionary)
