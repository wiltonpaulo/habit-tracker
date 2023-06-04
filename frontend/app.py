from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

# API endpoints
API_URL = os.environ.get('API_URL')

@app.route('/')
def index():
    habits = requests.get(f"{API_URL}/habits").json()
    return render_template('main.html', habits=habits)

@app.route('/add_habit', methods=['GET', 'POST'])
def add_habit():
    if request.method == 'POST':
        name = request.form['name']
        frequency = request.form['frequency']
        requests.post(f"{API_URL}/habits", json={'name': name, 'frequency': frequency})
        return redirect(url_for('index'))
    return render_template('add_habit.html')

@app.route('/edit_habit/<int:habit_id>', methods=['GET', 'POST'])
def edit_habit(habit_id):
    habit = requests.get(f"{API_URL}/habits/{habit_id}").json()
    if request.method == 'POST':
        name = request.form['name']
        frequency = request.form['frequency']
        requests.put(f"{API_URL}/habits/{habit_id}", json={'name': name, 'frequency': frequency})
        return redirect(url_for('index'))
    return render_template('edit_habit.html', habit=habit)

@app.route('/delete_habit/<int:habit_id>', methods=['GET', 'POST'])
def delete_habit(habit_id):
    requests.delete(f"{API_URL}/habits/{habit_id}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
