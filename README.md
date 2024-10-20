# Task Manager Fullstack Application

## Problem Statement

In today's fast-paced world, individuals need an efficient way to manage various aspects of their daily lives, such as keeping track of movies to watch, reading lists, content calendars, quick notes, and daily tasks. Existing solutions often lack simplicity or focus, making it difficult for users to manage their tasks efficiently in one place.

## Solution

The goal of this project is to develop a full-stack application that allows users to manage tasks, reading and movie lists, notes, and view calendars efficiently. The application will have a Flask API backend, supporting user interaction with data and providing a seamless user experience.

## MVP Features

1. As a user, I should only be able to perform CRUD operations on my own tasks, add a notification system where after a task is completed or almost due, the user gets a notification.
2. As a user, I can view a list of all my tasks, notes, movies, books, and calendar with all their statuses.
3. As a user, I can create a new list of daily tasks, notes, movies, books, and calendar.
4. As a user, I can delete a list of daily tasks, notes, movies, books, and calendar.
5. As a user, I can update a list of daily tasks, notes, movies, books, and calendar.
6. As a user, I can update the statuses of my list.

## Technical Specifications

1. Python (Flask)
2. PostgreSQL

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3.Set up the database:

Initialize the database:
# python app.py db init
Migrate the database:
# python app.py db migrate
Upgrade the database:
# python app.py db upgrade


## Registration Endpoint Example

To register a new user, send a POST request to the `/register` endpoint with the following JSON payload:

```json
{
  "email": "jane.smith@example.com",
  "password": "P@ssw0rd!"
}
```


## Login Endpoint Example

To login a registered user, send a POST request to the `/login` endpoint with the following JSON payload:

```json
{
  "email": "jane.smith@example.com",
  "password": "P@ssw0rd!"
}
```


```
This example uses a real-life email and password format.

# Quicknotes

### Create Quicknote

- **Method:** POST
- **URL:** `/quicknotes`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**

  ```json
  {
    "title": "Meeting Notes",
    "content": "Discussed project updates and set next meeting for Friday."
  }
  ```


### Get Quicknotes

- **Method:** GET
- **URL:** `/quicknotes`
- **Headers:**
  - `Authorization: Bearer <token>`

### Update Quicknote

- **Method:** PUT
- **URL:** `/quicknotes/{quicknote_id}`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "Updated Meeting Notes",
    "content": "Discussed project updates, set next meeting for Friday, and assigned tasks to team members."
  }
  ```

### Delete Quicknote

- **Method:** DELETE
- **URL:** `/quicknotes/{quicknote_id}`
- **Headers:**
  - `Authorization: Bearer <token>`

## Tasks

### Create Task

- **Method:** POST
- **URL:** `/tasks`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "Finish Project Report",
    "description": "Complete the project report and submit it by EOD.",
    "due_date": "2023-12-31T23:59:59Z"
  }
  ```

### Get Tasks

- **Method:** GET
- **URL:** `/tasks`
- **Headers:**
  - `Authorization: Bearer <token>`

### Update Task

- **Method:** PUT
- **URL:** `/tasks/{task_id}`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "Updated Project Report",
    "description": "Complete the project report, include financial data, and submit it by EOD.",
    "due_date": "2023-12-31T23:59:59Z",
    "completed": true
  }
  ```

### Delete Task

- **Method:** DELETE
- **URL:** `/tasks/{task_id}`
- **Headers:**
  - `Authorization: Bearer <token>`

## Movies

### Create Movie

- **Method:** POST
- **URL:** `/movies`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "Inception",
    "description": "A thief who steals corporate secrets through the use of dream-sharing technology.",
    "watched": false
  }
  ```

### Get Movies

- **Method:** GET
- **URL:** `/movies`
- **Headers:**
  - `Authorization: Bearer <token>`

### Update Movie

- **Method:** PUT
- **URL:** `/movies/{movie_id}`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "Inception",
    "description": "A thief who steals corporate secrets through the use of dream-sharing technology. Watched it last night.",
    "watched": true
  }
  ```

### Delete Movie

- **Method:** DELETE
- **URL:** `/movies/{movie_id}`
- **Headers:**
  - `Authorization: Bearer <token>`

## Books

### Create Book

- **Method:** POST
- **URL:** `/books`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "The Alchemist",
    "description": "A novel by Brazilian author Paulo Coelho that tells the story of Santiago, an Andalusian shepherd boy.",
    "read": false
  }
  ```

### Get Books

- **Method:** GET
- **URL:** `/books`
- **Headers:**
  - `Authorization: Bearer <token>`

### Update Book

- **Method:** PUT
- **URL:** `/books/{book_id}`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "The Alchemist",
    "description": "A novel by Brazilian author Paulo Coelho that tells the story of Santiago, an Andalusian shepherd boy. Finished reading it last week.",
    "read": true
  }
  ```

### Delete Book

- **Method:** DELETE
- **URL:** `/books/{book_id}`
- **Headers:**
  - `Authorization: Bearer <token>`

## Calendar Events

### Create Calendar Event

- **Method:** POST
- **URL:** `/calendar`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "Team Meeting",
    "description": "Discuss project progress and next steps.",
    "start_time": "2023-12-31T09:00:00Z",
    "end_time": "2023-12-31T10:00:00Z"
  }
  ```

### Get Calendar Events

- **Method:** GET
- **URL:** `/calendar`
- **Headers:**
  - `Authorization: Bearer <token>`

### Update Calendar Event

- **Method:** PUT
- **URL:** `/calendar/{event_id}`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body (raw JSON):**
  ```json
  {
    "title": "Updated Team Meeting",
    "description": "Discuss project progress, next steps, and assign tasks.",
    "start_time": "2023-12-31T09:00:00Z",
    "end_time": "2023-12-31T10:30:00Z"
  }
  ```

### Delete Calendar Event

- **Method:** DELETE
- **URL:** `/calendar/{event_id}`
- **Headers:**
  - `Authorization: Bearer <token>`

## Notifications

### Get Notifications

- **Method:** GET
- **URL:** `/notifications`
- **Headers:**
  - `Authorization: Bearer <token>`

These Postman prompts will allow you to perform all CRUD operations starting from sign up to notifications.

## Logout Endpoint Example

To logout an existing user, send a POST request to the `/logout` endpoint with the following JSON payload:

```json
{
  "email": "jane.smith@example.com",
  "password": "P@ssw0rd!"
}
