from flask import render_template, request, jsonify
from app import app

employees = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    employees.append(data)
    return jsonify(success=True)

@app.route('/display', methods=['GET'])
def display():
    return render_template