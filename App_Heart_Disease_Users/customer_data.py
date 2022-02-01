def data_collection():

    import pandas as pd


    user_data = {}

    while True:

        user_data["age"] = int(input("Enter age of the patient: "))
        user_data["sex"] = int(input("Enter sex of the patient Male: 1, Female: 0: "))
        user_data["trestbps"] = int(input("Enter trestbps of the patient: "))
        user_data["restecg"] = int(input("Enter restecg of the patient: "))
        user_data["thalach"] = int(input("Enter thalach of the patient: "))
        user_data["exang"] = int(input("Enter exang of the patient: "))
        user_data["oldpeak"] = float(input("Enter oldpeak of the patient: "))
        user_data["ca"] = int(input("Enter ca of the patient: "))
        user_data["cp_0"] = int(input("Enter cp of the patient cp: 1, 2, 3, 4: "))
        if user_data["cp_0"] == 1:
            user_data["cp_0"] = 1
            user_data["cp_1"] = 0
            user_data["cp_2"] = 0
            user_data["cp_3"] = 0
        elif user_data["cp_0"] == 2:
            user_data["cp_0"] = 0
            user_data["cp_1"] = 1
            user_data["cp_2"] = 0
            user_data["cp_3"] = 0
        elif user_data["cp_0"] == 3:
            user_data["cp_0"] = 0
            user_data["cp_1"] = 0
            user_data["cp_2"] = 1
            user_data["cp_3"] = 0
        elif user_data["cp_0"] == 4:
            user_data["cp_0"] = 0
            user_data["cp_1"] = 0
            user_data["cp_2"] = 0
            user_data["cp_3"] = 1

        user_data["thal_0"] = int(input("Enter thal of the patient thal: 0, 1, 2, 3: "))
        if user_data["thal_0"] == 0:
            user_data["thal_0"] = 1
            user_data["thal_1"] = 0
            user_data["thal_2"] = 0
            user_data["thal_3"] = 0
        elif user_data["thal_0"] == 1:
            user_data["thal_0"] = 0
            user_data["thal_1"] = 1
            user_data["thal_2"] = 0
            user_data["thal_3"] = 0
        elif user_data["thal_0"] == 2:
            user_data["thal_0"] = 0
            user_data["thal_1"] = 0
            user_data["thal_2"] = 1
            user_data["thal_3"] = 0
        elif user_data["thal_0"] == 3:
            user_data["thal_0"] = 0
            user_data["thal_1"] = 0
            user_data["thal_2"] = 0
            user_data["thal_3"] = 1

        user_data["slope_0"] = int(input("Enter slope of the patient slope: 0, 1, 2: "))
        if user_data["slope_0"] == 0:
            user_data["slope_0"] = 1
            user_data["slope_1"] = 0
            user_data["slope_2"] = 0
        elif user_data["slope_0"] == 1:
            user_data["slope_0"] = 0
            user_data["slope_1"] = 1
            user_data["slope_2"] = 0
        elif user_data["slope_0"] == 2:
            user_data["slope_0"] = 0
            user_data["slope_1"] = 0
            user_data["slope_2"] = 1
        
        break
        

    user_data_list = list(user_data.values())
    return user_data_list
"""
user_data_list = list(user_data.values())
print(type(user_data_list))
#df = pd.DataFrame(user_data)
#data = df.to_numpy()
#print(data.type())
#print(data)
prediction([user_data_list])
#prediction([[63, 1, 145, 0, 150, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]])

"""