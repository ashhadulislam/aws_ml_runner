import sys
import pandas as pd
import numpy as np
sys.path.insert(0,'utils/')
from qcri_helper import run_model
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route('/countme/<input_str>')
def count_me(input_str):
    return input_str


@app.route('/qcri/runmodel')
def qcri_runmodel():
    run_model()

    return "Loaded Model"


if __name__ == '__main__':
  #app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
  app.run(host="0.0.0.0",port=80,debug=True,use_reloader=False,threaded=False)



