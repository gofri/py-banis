import time
from flask import Flask, render_template, url_for, jsonify
import pyserver

app = Flask(__name__)

b = pyserver.Backend()

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', team=team_names)

@app.route('/status')
def status():
    global b
    return render_template('status.html', devices=updated_summary(b))

@app.route('/api/getJsonData')
def getJsonData():
    global b
    jsonData = jsonify(updated_summary(b))
    return jsonData

@app.route('/temp')
def temp():
    return render_template('temp.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    try:
        b.start()
        app.run(debug=True, use_reloader=False)
    finally:
        b.close()
