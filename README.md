# Superheroes
A simple Flask API for managing heroes, their powers, and the relationships between them using SQLAlchemy ORM and Flask-Migrate.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Contributing](#contributing)

## Project Overview
This API allows users to:
- Retrieve all heroes and their associated powers.
- Retrieve a specific hero or power by ID.
- Update power descriptions.
- Associate heroes with powers using predefined strength levels.

## Features
- **Flask**: Lightweight web framework.
- **SQLAlchemy ORM**: Database management and querying.
- **Flask-Migrate**: Handles database migrations.
- **SQLite**: Simple and efficient database storage.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pipenv (for managing dependencies)

### Steps
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <project_folder>
   ```

2. Install dependencies:
   ```sh
   pipenv install
   ```

## Database Setup
1. Initialize the database:
   ```sh
   pipenv run flask db init
   ```
2. Apply migrations:
   ```sh
   pipenv run flask db upgrade
   ```
3. Seed the database:
   ```sh
   pipenv run python seed.py
   ```

## Running the API
1. Activate the virtual environment:
   ```sh
   pipenv shell
   ```
2. Start the Flask server:
   ```sh
   python app.py
   ```
3. The API will be available at `http://127.0.0.1:5000/`

## API Endpoints
### Heroes
- **Get all heroes**: `GET /heroes`
- **Get a hero by ID**: `GET /heroes/<int:heroes_id>`

### Powers
- **Get all powers**: `GET /powers`
- **Get a power by ID**: `GET /powers/<int:powers_id>`
- **Update power description**: `PATCH /powers/<int:power_id>`

### Hero Powers
- **Assign power to hero**: `POST /hero_powers`
  ```json
  {
    "strength": "Strong",
    "power_id": 1,
    "hero_id": 1
  }
  ```

## Models
### Hero
- `id` (Integer, Primary Key)
- `name` (String, Required)
- `super_name` (String, Required)

### Power
- `id` (Integer, Primary Key)
- `name` (String, Required)
- `description` (String, Required, min 20 characters)

### HeroPower
- `id` (Integer, Primary Key)
- `strength` (String, Required: "Strong", "Weak", "Average")
- `hero_id` (Foreign Key to `heroes.id`)
- `power_id` (Foreign Key to `powers.id`)

## Contributing
Feel free to submit issues or contribute by making pull requests.


