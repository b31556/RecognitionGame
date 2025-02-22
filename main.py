from flask import Flask, render_template, request, session, send_file, redirect, jsonify
import os
import random
import time
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Cseréld le valós alkalmazásnál!

IMAGE_FOLDER = 'pic'
LOG_FOLDER = 'logs'

NUMBER_OF_QUESTIONS = 10


# you can manipulate what questions to ask to diferent persons
MANIPULATE = {
    "Nikoletta Horváth": ["kicsi_clue.png","Bepillogo.png","kicsi.png"]
}


chplayers=[]

chnames=[]

if "names.txt" in os.listdir() and "Players.txt" in os.listdir():
    with open("names.txt", "r") as f:
        for line in f:
            chnames.append(line.strip())
    with open("Players.txt", "r") as f:
        for line in f:
            chplayers.append(line.strip())

else:
    print("\n\n\nnames.txt or Players.txt not found!! make them!\n\n\n")
    raise FileNotFoundError




# Ellenőrizzük, hogy a log mappa létezik-e
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    session.clear()
    session['username'] = request.form['username']
    session['score'] = 0
    session['current_question'] = 0
    session['start_time'] = time.time()
    session['log_data'] = []
    
    if session['username'] in MANIPULATE:
        session['questions'] = MANIPULATE[session['username']]
    else:
        # Képek kiválasztása
        all_images = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
        random.shuffle(all_images)
        session['questions'] = all_images[:NUMBER_OF_QUESTIONS]
    
    return {'status': 'success'}

@app.route('/game')
def game():
    if not "username" in session:
        return redirect("/")
    return render_template("game.html",chnames=json.dumps(chnames),qnum=len(session['questions']))

@app.route('/get_question')
def get_question():
    if not "username" in session:
        return redirect("/")
    if 'current_question' not in session:
        return {'status': 'error'}, 400
    
    q_num = session['current_question']
    if q_num >= len(session["questions"]):
        return {'status': 'finished'}
    
    question_data = {
        'image': session['questions'][q_num],
        'question_number': q_num + 1
    }
    session['question_start'] = time.time()
    return question_data

@app.route('/answer', methods=['POST'])
def handle_answer():
    data = request.json
    user_answer = data['answer'].strip()
    q_num = session['current_question']
    correct_answer = os.path.splitext(session['questions'][q_num])[0]
    
    # Log adatok gyűjtése
    log_entry = {
        'question': q_num + 1,
        'image': session['questions'][q_num],
        'correct_answer': correct_answer,
        'user_answer': user_answer,
        'time_taken': round(time.time() - session['question_start'], 2)
    }
    
    if user_answer.lower() == correct_answer.lower():
        session['score'] += 1
        log_entry['correct'] = True
    else:
        log_entry['correct'] = False
    
    session['log_data'].append(log_entry)
    session['current_question'] += 1
    
    return {'status': 'success', 'correct': log_entry['correct'], "clue_picture":f"/images/{log_entry['image'].replace(".","_clue.")}"}

@app.route('/results')
def show_results():
    if not "username" in session:
        return redirect("/")
    # Log fájl létrehozása
    log_filename = f"{session['username']}_{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.txt"
    log_path = os.path.join(LOG_FOLDER, log_filename)
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(f"Player: {session['username']}\n")
        f.write(f"Total score: {session['score']}/{len(session['questions'])}\n")
        f.write("Details:\n")
        for entry in session['log_data']:
            f.write(
                f"Question {entry['question']}: "
                f"Image: {entry['image']}, "
                f"Correct: {entry['correct_answer']}, "
                f"Your answer: {entry['user_answer']}, "
                f"Time: {entry['time_taken']}s, "
                f"Correct: {'Yes' if entry['correct'] else 'No'}\n"
            )
    
    return render_template('results.html', 
                         score=session['score'],
                         log_data=session['log_data'],
                         username=session['username'],
                         qnum=len(session["questions"]))

@app.route('/images/<filename>')
def serve_image(filename):
    return send_file(os.path.join(IMAGE_FOLDER, filename))

@app.route('/get/<l>')
def get(l):
    if l == "names":
        return jsonify(chnames)
    elif l == 'players':
        return jsonify(chplayers)
    return "null"


@app.route('/<_>')
def not_found(_):
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)