from flask import Flask, abort
from flask import jsonify
from flask import request
import re

app = Flask(__name__)
empDB=[]

@app.route('/employee',methods=['GET'])
def getAllEmp():

    return jsonify({'emps':empDB})

@app.route('/employee/create',methods=['POST'])
def createEmp():
    if re.search(r'[\w.-]+@[\w.-]+\.[\w+]', request.json["email"]) and re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', request.json["birthdate"]) \
            and re.match('(\d{10}$)', request.json["phone"]["work"]) and re.match('(\d{10}$)', request.json["phone"]["personal"]):
        employeeData = {
        'name':request.json['name'],
        'company':request.json['company'],
        'image': request.json['image'],
        'phone': request.json['phone'],
        'address': request.json['address'],
        'email': request.json['email'],
        'birthdate': request.json['birthdate']
        }
        empDB.append(employeeData)
    else:
        abort(404)

    return jsonify(employeeData)

@app.route('/employee/<name>',methods=['GET'])
def getEmp(name):

    print(name)
    print(empDB)
    usr = [ emp for emp in empDB if (emp['name'] == name) ]
    print(usr)
    if len(usr) == 0:
       abort(404)
    return jsonify({'emp':usr})

@app.route('/employee/<name>',methods=['PUT'])
def updateEmp(name):

    em = [ emp for emp in empDB if (emp['name'] == name) ]
    if len(em) == 0:
       abort(404)
    for i in request.json:
        em[0][i] = request.json[i]
    return jsonify({'emp':em[0]})

@app.route('/employee/<name>',methods=['DELETE'])
def deleteEmp(name):

    em = [ emp for emp in empDB if (emp['name'] == name) ]
    if len(em) == 0:
       abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})

@app.route('/employee/search/<strng>',methods=['GET'])
def searchEmp(strng):
    if re.search(r'[\w.-]+@[\w.-]+\.[\w+]|(\d{10}$)', strng):
        usr = [ emp for emp in empDB if (emp['email'] == strng or emp['phone']['work'] == strng or emp['phone']['personal'] == strng) ]
        if len(usr) == 0:
            abort(404)
    else:
        abort(404)
    return jsonify({'emp':usr})

@app.route('/employee/searchadd/<strr>',methods=['GET'])
def searchEmpAdd(strr):

    usr = [ emp for emp in empDB if (emp['address']['city'] == strr or emp['address']['state'] == strr) ]
    if len(usr) == 0:
       abort(404)
    return jsonify({'emp':usr})



if __name__ == '__main__':
 app.run()