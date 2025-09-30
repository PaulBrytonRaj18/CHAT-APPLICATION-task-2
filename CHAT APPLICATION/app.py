from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_socketio import SocketIO, emit, join_room, leave_room
import uuid
import json
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory storage (in production, use a database)
users = {}  # {user_id: {'password': password, 'rooms': set(), 'online': False}}
rooms = {}  # {room_code: {'name': name, 'users': set(), 'messages': []}}
active_connections = {}  # {session_id: user_id}

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id', '').strip()
        password = request.form.get('password', '').strip()
        
        if not user_id or not password:
            flash('Please fill in all fields', 'error')
            return render_template('login.html')
        
        if user_id in users and users[user_id]['password'] == password:
            session['user_id'] = user_id
            users[user_id]['online'] = True
            flash(f'Welcome back, {user_id}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid user ID or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('user_id', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()
        
        if not user_id or not password or not confirm_password:
            flash('Please fill in all fields', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('register.html')
        
        if len(password) < 4:
            flash('Password must be at least 4 characters long', 'error')
            return render_template('register.html')
        
        if user_id in users:
            flash('User ID already exists', 'error')
            return render_template('register.html')
        
        users[user_id] = {
            'password': password,
            'rooms': set(),
            'online': True
        }
        
        session['user_id'] = user_id
        flash(f'Account created successfully! Welcome, {user_id}!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    try:
        if 'user_id' not in session:
            print("No user_id in session, redirecting to login")
            return redirect(url_for('login'))
        
        user_id = session['user_id']
        print(f"Dashboard accessed by user: {user_id}")
        
        # Check if user exists in users dictionary
        if user_id not in users:
            print(f"User {user_id} not found in users dictionary")
            flash('User session expired. Please login again.', 'error')
            session.pop('user_id', None)
            return redirect(url_for('login'))
        
        user_rooms = list(users[user_id]['rooms'])
        print(f"User {user_id} has rooms: {user_rooms}")
        print(f"Total rooms available: {list(rooms.keys())}")
        
        # Pass rooms dictionary to template for room names
        return render_template('dashboard.html', 
                             user_id=user_id, 
                             user_rooms=user_rooms,
                             rooms=rooms,
                             all_rooms=list(rooms.keys()))
    except Exception as e:
        print(f"Error in dashboard route: {str(e)}")
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('login'))

@app.route('/room/<room_code>')
def room(room_code):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    
    if room_code not in rooms:
        flash('Room not found', 'error')
        return redirect(url_for('dashboard'))
    
    if user_id not in users:
        flash('User not found', 'error')
        return redirect(url_for('login'))
    
    # Add user to room if not already in it
    if room_code not in users[user_id]['rooms']:
        users[user_id]['rooms'].add(room_code)
        rooms[room_code]['users'].add(user_id)
    
    return render_template('room.html', 
                         room_code=room_code, 
                         room_name=rooms[room_code]['name'],
                         user_id=user_id,
                         messages=rooms[room_code]['messages'])

@app.route('/logout')
def logout():
    if 'user_id' in session:
        user_id = session['user_id']
        if user_id in users:
            users[user_id]['online'] = False
        session.pop('user_id', None)
    return redirect(url_for('index'))

# WebSocket Events
@socketio.on('connect')
def handle_connect():
    if 'user_id' in session:
        user_id = session['user_id']
        active_connections[request.sid] = user_id
        users[user_id]['online'] = True
        print(f'User {user_id} connected')

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in active_connections:
        user_id = active_connections[request.sid]
        users[user_id]['online'] = False
        del active_connections[request.sid]
        print(f'User {user_id} disconnected')

@socketio.on('join_room')
def handle_join_room(data):
    room_code = data.get('room_code')
    user_id = session.get('user_id')
    
    if not user_id or room_code not in rooms:
        return
    
    join_room(room_code)
    emit('user_joined', {
        'user_id': user_id,
        'message': f'{user_id} joined the room',
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room=room_code)

@socketio.on('leave_room')
def handle_leave_room(data):
    room_code = data.get('room_code')
    user_id = session.get('user_id')
    
    if not user_id:
        return
    
    leave_room(room_code)
    emit('user_left', {
        'user_id': user_id,
        'message': f'{user_id} left the room',
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room=room_code)

@socketio.on('send_message')
def handle_message(data):
    room_code = data.get('room_code')
    message = data.get('message', '').strip()
    user_id = session.get('user_id')
    
    if not user_id or not message or room_code not in rooms:
        return
    
    message_data = {
        'user_id': user_id,
        'message': message,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }
    
    # Store message in room history
    rooms[room_code]['messages'].append(message_data)
    
    # Emit to all users in the room
    emit('new_message', message_data, room=room_code)

@socketio.on('create_room')
def handle_create_room(data):
    room_name = data.get('room_name', '').strip()
    user_id = session.get('user_id')
    
    if not user_id or not room_name:
        return
    
    # Generate unique room code
    room_code = str(uuid.uuid4())[:8].upper()
    
    rooms[room_code] = {
        'name': room_name,
        'users': {user_id},
        'messages': []
    }
    
    users[user_id]['rooms'].add(room_code)
    
    emit('room_created', {
        'room_code': room_code,
        'room_name': room_name
    })

@socketio.on('join_existing_room')
def handle_join_existing_room(data):
    room_code = data.get('room_code', '').strip().upper()
    user_id = session.get('user_id')
    
    if not user_id or room_code not in rooms:
        emit('join_error', {'message': 'Invalid room code'})
        return
    
    users[user_id]['rooms'].add(room_code)
    rooms[room_code]['users'].add(user_id)
    
    emit('room_joined', {
        'room_code': room_code,
        'room_name': rooms[room_code]['name'],
        'messages': rooms[room_code]['messages']
    })

if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0', port=5000)
