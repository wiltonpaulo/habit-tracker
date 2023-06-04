# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY frontend/requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY frontend .

# Expose the port on which the application will run
EXPOSE 5001

# Set the command to run the application
CMD ["python", "app.py"]
