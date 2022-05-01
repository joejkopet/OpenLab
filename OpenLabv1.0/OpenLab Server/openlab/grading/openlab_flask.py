import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask
application = Flask(__name__)

def classnamehere_student1_LP1_1():
    stdout = check_output(['OpenLab Server\openlab\grading\classes\classnamehere\template_student1_LP1_1.sh']).decode('utf-8')
    return stdout

@application.route('/classnamehere/student1_LP1_1',methods=['GET',])
def home():
    return '<pre>'+classnamehere_student1_LP1_1()+'</pre>'

if __name__ == '_main_':
   application.run(host='0.0.0.0',port=5005,debug=True)
