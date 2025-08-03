from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
import openai

openai.api_key = "secret"

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

@index_views.route('/chat', methods=['POST'])
def openai_chat():
    data = request.get_json()
    messages = data.get('messages', [])

    # Preprompt for RAG simulation on course data
    preprompt = {
        "role": "system",
        "content": (
            "You are a university course assistant with access to a knowledge base of course, staff, and enrolment data. "
            "You answer questions using the following dummy data:\n"
            "- COMP1601: Intro to Programming, Lecturer: Dr. Smith, Enrolment: 120, Avg Grade: 75\n"
            "- COMP1602: Data Structures, Lecturer: Dr. Jones, Enrolment: 100, Avg Grade: 70\n"
            "- COMP2603: Databases, Lecturer: Dr. Lee, Enrolment: 80, Avg Grade: 68\n"
            "- Staff: Dr. Smith, Dr. Jones, Dr. Lee, Ms. Brown (TA)\n"
            "- Semester: 2023/2024-II\n"
            "If you don't know the answer, say so. Respond as if you are retrieving from this data."
        )
    }

    # Always insert the preprompt as the first message
    full_messages = [preprompt] + [m for m in messages if m.get("role") != "system"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=full_messages
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': "Sorry, there was an error contacting OpenAI."}), 500