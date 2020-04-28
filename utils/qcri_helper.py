import pandas as pd
from keras.models import load_model

def run_model():
    model=load_model("/home/ubuntu/projects/test_scripts/test_qcri/pkls/mlp_elu_30Mar_thres0.005.p")


