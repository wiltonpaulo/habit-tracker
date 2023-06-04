# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY backend/requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY backend .

# Expose the port that the Flask application will run on
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["flask", "run"]
