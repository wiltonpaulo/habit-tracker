from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)
api = Api(app)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    frequency = db.Column(db.String(100), nullable=False)

    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

class HabitResource(Resource):
    def get(self, habit_id=None):
        if habit_id:
            habit = Habit.query.get(habit_id)
            if habit:
                return {'id': habit.id, 'name': habit.name, 'frequency': habit.frequency}
            else:
                return {'message': 'Habit not found'}, 404
        else:
            habits = Habit.query.all()
            habit_list = [{'id': habit.id, 'name': habit.name, 'frequency': habit.frequency} for habit in habits]
            return habit_list

    def post(self):
        data = request.get_json()
        name = data.get('name')
        frequency = data.get('frequency')

        habit = Habit(name, frequency)
        db.session.add(habit)
        db.session.commit()

        return {'message': 'Habit created successfully'}, 201

    def put(self, habit_id):
        habit = Habit.query.get(habit_id)
        if habit:
            data = request.get_json()
            habit.name = data.get('name', habit.name)
            habit.frequency = data.get('frequency', habit.frequency)
            db.session.commit()
            return {'message': 'Habit updated successfully'}
        else:
            return {'message': 'Habit not found'}, 404

    def delete(self, habit_id):
        habit = Habit.query.get(habit_id)
        if habit:
            db.session.delete(habit)
            db.session.commit()
            return {'message': 'Habit deleted successfully'}
        else:
            return {'message': 'Habit not found'}, 404

api.add_resource(HabitResource, '/habits', '/habits/<int:habit_id>')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
