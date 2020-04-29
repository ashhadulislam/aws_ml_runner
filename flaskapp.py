import sys
sys.path.insert(0,'utils/')

import pandas as pd
import numpy as np
import config

from qcri_helper import run_model
import flask
from flask import Flask,render_template, jsonify, request
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

@app.route('/api/v1/qcri/runmodel/single', methods=['POST','GET'])
def api_qcri_runmodel_single():    
    if flask.request.method == 'GET':
        req_data = None
    elif flask.request.method == 'POST':
        req_data = request.get_json()
    results=run_model(req_data)

    return jsonify(results)



@app.route('/qcri_submit_vitals',methods=["POST"])
def qcri_submit_vitals():
  req_data = request.form.to_dict()
  results=run_model(req_data)
  # print("Details are: ",req_data)
  return render_template("qcri_vital_enter.html", items=results)




@app.route('/qcri/testvital')
def qcri_testvital():
    return render_template('qcri_vital_enter.html')


if __name__ == '__main__':
  app.run(host="0.0.0.0",port=80,debug=True,use_reloader=False,threaded=False)
  #app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
  # if config.env=="local":
  #     # app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
  #     app.run(host="0.0.0.0",port=80,debug=True,use_reloader=False,threaded=False)
  # elif config.env=="aws":
  #     app.run(host="0.0.0.0",port=80,debug=True,use_reloader=False,threaded=False)



