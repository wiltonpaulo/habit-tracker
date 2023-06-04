# Get all habits
curl -X GET http://localhost:5000/habit

# Get a specific habit
curl -X GET http://localhost:5000/habit/1

# Create a new habit
curl -X POST -H "Content-Type: application/json" -d '{"name": "Exercise", "frequency": "daily"}' http://localhost:5000/habits

# Update an existing habit
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Exercise", "frequency": "weekly"}' http://localhost:5000/habits/1

# Delete a habit
curl -X DELETE http://localhost:5000/habit/1
