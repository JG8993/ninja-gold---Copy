from flask import Flask, render_template, redirect, session, request
import random
import datetime
app= Flask(__name__)

app.secret_key = "i like turtles"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    current_time=datetime.datetime.now()
    if "count" not in session:
        session["count"] = 0
    if request.form['building'] == 'farm':
        session["count"] += random.randint(10,20) 
    elif request.form['building'] == 'cave':
        session["count"] += random.randint(5,10)
    elif request.form['building'] == 'house':
        session["count"] += random.randint(2,5)
    elif request.form['building'] == 'casino':
        session["count"] += random.randint(-50,50)
    message = (f"You've earned {session['count']} gold {current_time}")
    return render_template("index.html", message=message)

@app.route('/reset')
def reset_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
