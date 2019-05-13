from flask import Flask, Blueprint, jsonify
from flask import render_template, request
import json
import ast

insight_controller = Blueprint('insight_controller', __name__)

@insight_controller.route('/')
def insight_index():
    return render_template('insight/index.html')

@insight_controller.route('/data/history')
def insight_data_history():
    with open('static/model_history/history.json', 'r') as file:
        op = json.load(file)
    return jsonify(op)

@insight_controller.route('/data/report')
def insight_data_report():
    with open('static/model_history/classification_report.json', 'r') as file:
        op = json.load(file)
    return jsonify(op)

@insight_controller.route('/data/confusion_matrix')
def insight_data_confusion_matrix():
    with open('static/model_history/confusion_matrix.json', 'r') as file:
        op = json.load(file)
    return jsonify(op)

@insight_controller.route('/data/current_situation')
def insight_data_current_situation():
    with open('static/model_history/situation.json', 'r') as file:
        cs = json.load(file)
    return jsonify(cs)