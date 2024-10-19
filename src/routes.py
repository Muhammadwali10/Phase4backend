from flask import Blueprint, request, jsonify
from .models import db, Quicknote, User, Task, Movie, Book, CalendarEvent, Notification
from flask_login import login_required, current_user
from datetime import datetime

quicknotes_bp = Blueprint('quicknotes', __name__)
tasks_bp = Blueprint('tasks', __name__)
movies_bp = Blueprint('movies', __name__)
books_bp = Blueprint('books', __name__)
calendar_bp = Blueprint('calendar', __name__)
notifications_bp = Blueprint('notifications', __name__)

# Quicknotes CRUD Operations
@quicknotes_bp.route('/quicknotes', methods=['POST'])
@login_required
def create_quicknote():
    data = request.get_json()
    new_quicknote = Quicknote(title=data['title'], content=data['content'], user_id=current_user.id)
    db.session.add(new_quicknote)
    db.session.commit()
    return jsonify({'message': 'Quicknote created successfully'}), 201

@quicknotes_bp.route('/quicknotes', methods=['GET'])
@login_required
def get_quicknotes():
    quicknotes = Quicknote.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': q.id, 'title': q.title, 'content': q.content, 'created_at': q.created_at} for q in quicknotes]), 200

@quicknotes_bp.route('/quicknotes/<int:id>', methods=['PUT'])
@login_required
def update_quicknote(id):
    data = request.get_json()
    quicknote = Quicknote.query.filter_by(id=id, user_id=current_user.id).first()
    if not quicknote:
        return jsonify({'message': 'Quicknote not found'}), 404
    quicknote.title = data['title']
    quicknote.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Quicknote updated successfully'}), 200

@quicknotes_bp.route('/quicknotes/<int:id>', methods=['DELETE'])
@login_required
def delete_quicknote(id):
    quicknote = Quicknote.query.filter_by(id=id, user_id=current_user.id).first()
    if not quicknote:
        return jsonify({'message': 'Quicknote not found'}), 404
    db.session.delete(quicknote)
    db.session.commit()
    return jsonify({'message': 'Quicknote deleted successfully'}), 200

# Tasks CRUD Operations
@tasks_bp.route('/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.get_json()
    due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
    new_task = Task(title=data['title'], description=data['description'], due_date=due_date, user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

@tasks_bp.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': t.id, 'title': t.title, 'description': t.description, 'due_date': t.due_date, 'completed': t.completed} for t in tasks]), 200

@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
@login_required
def update_task(id):
    data = request.get_json()
    task = Task.query.filter_by(id=id, user_id=current_user.id).first()
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    task.title = data['title']
    task.description = data['description']
    task.due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
    task.completed = data['completed']
    task.check_for_notifications()
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'}), 200

@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first()
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200

# Movies CRUD Operations
@movies_bp.route('/movies', methods=['POST'])
@login_required
def create_movie():
    data = request.get_json()
    new_movie = Movie(title=data['title'], description=data['description'], watched=data['watched'], user_id=current_user.id)
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({'message': 'Movie created successfully'}), 201

@movies_bp.route('/movies', methods=['GET'])
@login_required
def get_movies():
    movies = Movie.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': m.id, 'title': m.title, 'description': m.description, 'watched': m.watched} for m in movies]), 200

@movies_bp.route('/movies/<int:id>', methods=['PUT'])
@login_required
def update_movie(id):
    data = request.get_json()
    movie = Movie.query.filter_by(id=id, user_id=current_user.id).first()
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    movie.title = data['title']
    movie.description = data['description']
    movie.watched = data['watched']
    db.session.commit()
    return jsonify({'message': 'Movie updated successfully'}), 200

@movies_bp.route('/movies/<int:id>', methods=['DELETE'])
@login_required
def delete_movie(id):
    movie = Movie.query.filter_by(id=id, user_id=current_user.id).first()
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted successfully'}), 200

# Books CRUD Operations
@books_bp.route('/books', methods=['POST'])
@login_required
def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'], description=data['description'], read=data['read'], user_id=current_user.id)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully'}), 201

@books_bp.route('/books', methods=['GET'])
@login_required
def get_books():
    books = Book.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': b.id, 'title': b.title, 'description': b.description, 'read': b.read} for b in books]), 200

@books_bp.route('/books/<int:id>', methods=['PUT'])
@login_required
def update_book(id):
    data = request.get_json()
    book = Book.query.filter_by(id=id, user_id=current_user.id).first()
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    book.title = data['title']
    book.description = data['description']
    book.read = data['read']
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'}), 200

@books_bp.route('/books/<int:id>', methods=['DELETE'])
@login_required
def delete_book(id):
    book = Book.query.filter_by(id=id, user_id=current_user.id).first()
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 200

# Calendar Events CRUD Operations
@calendar_bp.route('/calendar', methods=['POST'])
@login_required
def create_calendar_event():
    data = request.get_json()
    new_event = CalendarEvent(title=data['title'], description=data['description'], start_time=datetime.fromisoformat(data['start_time'].replace('Z', '+00:00')), end_time=datetime.fromisoformat(data['end_time'].replace('Z', '+00:00')), user_id=current_user.id)
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Calendar event created successfully'}), 201

@calendar_bp.route('/calendar', methods=['GET'])
@login_required
def get_calendar_events():
    events = CalendarEvent.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': e.id, 'title': e.title, 'description': e.description, 'start_time': e.start_time, 'end_time': e.end_time} for e in events]), 200

@calendar_bp.route('/calendar/<int:id>', methods=['PUT'])
@login_required
def update_calendar_event(id):
    data = request.get_json()
    event = CalendarEvent.query.filter_by(id=id, user_id=current_user.id).first()
    if not event:
        return jsonify({'message': 'Calendar event not found'}), 404
    event.title = data['title']
    event.description = data['description']
    event.start_time = datetime.fromisoformat(data['start_time'].replace('Z', '+00:00'))
    event.end_time = datetime.fromisoformat(data['end_time'].replace('Z', '+00:00'))
    db.session.commit()
    return jsonify({'message': 'Calendar event updated successfully'}), 200

@calendar_bp.route('/calendar/<int:id>', methods=['DELETE'])
@login_required
def delete_calendar_event(id):
    event = CalendarEvent.query.filter_by(id=id, user_id=current_user.id).first()
    if not event:
        return jsonify({'message': 'Calendar event not found'}), 404
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Calendar event deleted successfully'}), 200

# Notifications CRUD Operations
@notifications_bp.route('/notifications', methods=['GET'])
@login_required
def get_notifications():
    notifications = Notification.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': n.id, 'message': n.message, 'created_at': n.created_at} for n in notifications]), 200
