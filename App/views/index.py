from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('login.html')

@index_views.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@index_views.route('/chat', methods=['GET'])
def chat():
    return render_template('chat.html')

@index_views.route('/project', methods=['GET'])
def projections():
    return render_template('projections.html')

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})