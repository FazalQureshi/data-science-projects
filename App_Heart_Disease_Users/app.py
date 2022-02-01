import pickle # this module allows to serialize your model into a file



with open('model_pickle','rb') as file: # 'rb''  read a binary # with file pointer
    mp = pickle.load(file) 


from customer_data import data_collection

customer_list = data_collection()



patient_prediction = mp.predict([customer_list])

if patient_prediction == [0]:
    
    print("-"*70)
    print("\n\n\n--------> The pateint is predicted NOT to have a Heart Disease <--------\n\n\n")
    print("-"*70)
else:
    print("-"*70)
    print("\n\n\n--------> The patient is predicted to have a Heart Disease <--------\n\n\n")
    print("-"*70)


