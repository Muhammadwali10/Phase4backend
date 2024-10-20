from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from src.models import db, User
from src.routes import quicknotes_bp, tasks_bp, movies_bp, books_bp, calendar_bp, notifications_bp
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS
import traceback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quicknotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
db.init_app(app)
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'Email already exists'}), 409

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        print(f"New user added to session: {new_user.email}")  # Debug statement
        db.session.commit()
        print("User committed to database")  # Debug statement
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        print(f"Error during registration: {e}")
        traceback.print_exc()  # Print the full traceback
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'message': 'An internal server error occurred. Please try again later.'}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Logged in successfully', 'token': access_token}), 200
    return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

app.register_blueprint(quicknotes_bp)
app.register_blueprint(tasks_bp)
app.register_blueprint(movies_bp)
app.register_blueprint(books_bp)
app.register_blueprint(calendar_bp)
app.register_blueprint(notifications_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
