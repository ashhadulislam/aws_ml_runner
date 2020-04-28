import pandas as pd
from keras.models import load_model
import config
from numpy import array

test_data={
    "occ_acc":0,
    "time_sitting_weekend_comp":2,
    "typ_sleep_last_yr":2,
    "nap_day_last_yr":5,
    "snore":1,
    "other_house_smoker":1,
    "father_alive":3,
    "age":42,
    "hipwaist_waist_size":85,
    "hipwaist_hip_size":99,
    "diastolic_bp1":76,
    "diastolic_bp2":69,
    "systolic_bp1":111,
    "bmi":26.2
}


def run_model(req_data):

    model=load_model(config.qcri_pkl_location)
    if req_data!=None:
        global test_data
        test_data=req_data
    list_features=[]
    for key,val in test_data.items():
        list_features.append(val)
    Xnew = array([list_features])

    ynew = model.predict_classes(Xnew)
    yproba = model.predict_proba(Xnew)
    # show the inputs and predicted outputs
    print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))
    print("probability=",yproba)
    print("Over and out")
    result_dict={"data":test_data,"class":str(ynew[0]),
    "control":str(yproba[0][0]),"case":str(yproba[0][1])}



    return result_dict


