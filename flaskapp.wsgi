#flaskapp.wsgi
activate_this = '/home/ubuntu/venv_face_rec/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
import sys
sys.path.insert(0, '/var/www/html/flaskapp')
sys.path.insert(0, '/home/ubuntu/projects/face_rec_flask/flask_ebs/utils')


from flaskapp import app as application
