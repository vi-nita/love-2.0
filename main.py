import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def homepage():
  return render_template('index.html')

@app.route("/index.html")
def admin():
  return redirect(url_for("homepage"))


@app.route("/write.html", methods=['POST', 'GET'])
def home():
  if request.method == 'POST':
    message = request.form['message']
    with open('data.txt', 'a') as file:
      file.write(message + ' \n')
    return redirect(url_for('home', message=message))
  return render_template('write.html')


@app.route('/view.html')
def encouragement():
  with open('data.txt') as f:
       phrases = [phrase.strip() for phrase in f.readlines()]
       phrase = random.choice(phrases)
  return render_template ('view.html',phrase=phrase)


@app.route('/goodbye')
def goodbye():
    return render_template('goodbye.html')

@app.route('/entertain.html')
def entertain():
  return render_template('entertain.html')

app.run(host='0.0.0.0', port=80)
