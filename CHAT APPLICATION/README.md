# ChatApp - Real-time Chat Application

A modern, real-time chat application built with Flask and WebSocket technology. Features include user authentication, room creation, and instant messaging.

## Features

- **User Authentication**: Create unique user accounts with custom IDs and passwords
- **Room Management**: Create new chat rooms and join existing ones with room codes
- **Real-time Messaging**: Instant messaging using WebSocket technology
- **Modern UI**: Beautiful, responsive design with a gradient theme
- **Message History**: View chat history when entering rooms
- **Online Status**: See who's online in real-time

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://localhost:5000`

## Usage

### Getting Started

1. **Create an Account**: 
   - Click "Create Account" on the home page
   - Choose a unique User ID and password
   - Your User ID will be your identifier in the chat

2. **Login**:
   - Use your User ID and password to login
   - You'll be redirected to your dashboard

### Creating Rooms

1. **From the Dashboard**:
   - Enter a room name in the "Create New Room" section
   - Click "Create Room"
   - You'll get a unique room code to share with others

2. **Sharing Room Codes**:
   - Copy the room code and share it with friends
   - They can use this code to join your room

### Joining Rooms

1. **Using Room Code**:
   - Enter the room code in the "Join Existing Room" section
   - Click "Join Room"
   - You'll be taken directly to the chat room

### Chatting

1. **Sending Messages**:
   - Type your message in the input field at the bottom
   - Press Enter or click the send button
   - Messages appear instantly for all room members

2. **Viewing History**:
   - All messages are saved in the room
   - When you enter a room, you'll see the message history
   - Scroll up to see older messages

## Technical Details

### Backend
- **Flask**: Web framework for handling HTTP requests
- **Flask-SocketIO**: WebSocket support for real-time communication
- **Eventlet**: Async server for handling concurrent connections

### Frontend
- **HTML5/CSS3**: Modern, responsive design
- **JavaScript**: Client-side interactivity
- **Socket.IO**: Real-time communication with the server
- **Font Awesome**: Icons for better UX

### Data Storage
- **In-memory storage**: Users, rooms, and messages are stored in memory
- **Session management**: User sessions are handled securely
- **Note**: Data is lost when the server restarts (use a database for production)

## File Structure

```
ChatApp/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── dashboard.html    # User dashboard
│   └── room.html         # Chat room page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── app.js        # JavaScript utilities
```

## Customization

### Changing the Theme
Edit `static/css/style.css` to modify colors, fonts, and layout:
- Main gradient: Lines 135-136
- Primary color: `#667eea` (used throughout)
- Secondary colors: Various shades of blue and purple

### Adding Features
- **Database integration**: Replace in-memory storage with SQLite/PostgreSQL
- **File sharing**: Add support for image/file uploads
- **Private messages**: Implement direct messaging between users
- **User profiles**: Add profile pictures and status messages

## Security Considerations

For production use, consider:
- Using a proper database (SQLite, PostgreSQL, etc.)
- Implementing HTTPS
- Adding rate limiting
- Input validation and sanitization
- Session security improvements
- Environment variables for sensitive data

## Troubleshooting

### Common Issues

1. **Port already in use**:
   - Change the port in `app.py` (line 156)
   - Or stop other services using port 5000

2. **Dependencies not installing**:
   - Make sure you're using Python 3.7+
   - Try using a virtual environment

3. **WebSocket connection issues**:
   - Check browser console for errors
   - Ensure firewall isn't blocking the connection

### Getting Help

- Check the browser console for JavaScript errors
- Look at the terminal running the Flask app for server errors
- Ensure all dependencies are installed correctly

## License

This project is open source and available under the MIT License.
