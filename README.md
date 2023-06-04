# Habit Tracker Application

<img src="frontend/static/logo.png" alt="Habit Tracker" width="100">

The Habit Tracker is a comprehensive habit tracking web application designed to help users establish and track their daily habits. This project was developed as part of a study on Python programming and web development.

## Motivation

The main motivations behind this project include:

- Personal Development: Enhancing Python programming skills and gaining hands-on experience with building a full-stack web application.
- Habit Tracking: Creating a basic habit tracking app (still improving it).
- Learning and Exploration: Exploring the use of popular frameworks and technologies such as Flask, Bootstrap, and Docker.

## Features

The Habit Tracker includes the following key features:

- Habit Management: Users can create, view, edit, and delete their habits.
- Frequency Tracking: Each habit can be tracked on a daily, weekly, or monthly basis.
- User-Friendly Interface: The application provides an intuitive user interface for easy habit management and tracking.
- Responsive Design: The frontend is built using Bootstrap to ensure a responsive and mobile-friendly experience.
- Containerization: The application is containerized using Docker for easy deployment and scalability.

## Getting Started

### Prerequisites

Before running the application, ensure that you have the following dependencies installed:

- Docker: Install Docker by following the instructions [here](https://docs.docker.com/get-docker/).
- Docker Compose: Install Docker Compose by following the instructions [here](https://docs.docker.com/compose/install/).

### Running the Application

To run the application, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/wiltonpaulo/habit-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd habit-tracker
   ```

3. Build and run the application using Docker Compose:

   ```bash
   docker-compose up --build
   ```

4. Access the application in your web browser at:
   - Backend API: `http://localhost:5000`
   - Frontend UI: `http://localhost:5001`

### Docker Compose Commands

Use the following Docker Compose commands for managing the application:

- Start the application: `docker-compose up`
- Stop the application: Press `Ctrl + C` in the terminal where the application is running.
- Clean up the resources (containers, networks, and volumes): `docker-compose down`

For more details on using Docker Compose, refer to the [Docker Compose documentation](https://docs.docker.com/compose/).

## Directory Structure

The project directory has the following structure:

- `backend/`: Contains the backend API code and configuration files.
  - `Dockerfile`: Dockerfile for building the backend container.
  - `app.py`: Main Python script for the Flask backend.
  - `requirements.txt`: Python dependencies for the backend.

- `frontend/`: Contains the frontend UI code and assets.
  - `Dockerfile`: Dockerfile for building the frontend container.
  - `app.py`: Main Python script for the Flask frontend.
  - `requirements.txt`: Python dependencies for the frontend.
  - `static/`: Static assets such as CSS, JS, and images.
    - `css/`: CSS stylesheets for the frontend.
    - `logo.png`: Logo image for the application.
    - `main.js`: JavaScript file for frontend functionality.
    - `style.css`: Custom CSS styles for the application.
  - `templates/`: HTML templates for the frontend pages.
    - `add_habit.html`: Page for adding a new habit.
    - `edit_habit.html`: Page for editing an existing habit.
    - `footer.html`: Footer component for the application.
    - `habits.html`: Page for viewing and managing habits.
    - `header.html`: Header component for the application.
    - `main.html`: Main template for the application.

- `docker-compose.yaml`: Docker Compose configuration file for running the application.
- `requirements.txt`: Python dependencies for the entire project.
- `scripts/`: Contains any additional scripts or database initialization files.
  - `init.db.sql`: SQL script for initializing the database.

## License

This project is licensed under the [MIT License](LICENSE).
