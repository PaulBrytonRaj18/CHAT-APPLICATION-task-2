# ChatApp Demo Guide

## Quick Start

1. **Install and Run**:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

2. **Open Browser**: Go to `http://localhost:5000`

## Demo Steps

### Step 1: Create First User
1. Click "Create Account"
2. User ID: `alice`
3. Password: `password123`
4. Click "Create Account"

### Step 2: Create a Room
1. You'll be redirected to the dashboard
2. In "Create New Room" section:
   - Room Name: `General Chat`
3. Click "Create Room"
4. You'll get a room code (e.g., `A1B2C3D4`)
5. Copy this code!

### Step 3: Create Second User
1. Open a new browser tab/window
2. Go to `http://localhost:5000`
3. Click "Create Account"
4. User ID: `bob`
5. Password: `password123`
6. Click "Create Account"

### Step 4: Join the Room
1. In Bob's dashboard, scroll to "Join Existing Room"
2. Enter the room code from Step 2
3. Click "Join Room"

### Step 5: Start Chatting!
1. Both users are now in the same room
2. Type messages and see them appear instantly
3. Try sending messages from both users
4. Notice the real-time updates!

## Features to Test

### ✅ User Management
- [x] Create unique user accounts
- [x] Login with user ID and password
- [x] Session management

### ✅ Room Management
- [x] Create new chat rooms
- [x] Generate unique room codes
- [x] Join existing rooms with codes
- [x] View room history

### ✅ Real-time Chat
- [x] Instant message delivery
- [x] Message history preservation
- [x] User join/leave notifications
- [x] WebSocket connectivity

### ✅ UI/UX
- [x] Responsive design
- [x] Beautiful gradient theme
- [x] Modern interface
- [x] Intuitive navigation

## Advanced Testing

### Multiple Rooms
1. Create multiple rooms with different names
2. Join different rooms in different tabs
3. Verify messages stay in their respective rooms

### Multiple Users
1. Create 3-4 different user accounts
2. Have all users join the same room
3. Test group chat functionality

### Room Codes
1. Try joining with invalid room codes
2. Test case sensitivity (should be case-insensitive)
3. Verify room codes are unique

## Troubleshooting

### Common Issues
- **Can't connect**: Make sure Flask app is running
- **Messages not appearing**: Check browser console for errors
- **Room not found**: Verify room code is correct

### Browser Requirements
- Modern browser with WebSocket support
- JavaScript enabled
- No ad blockers blocking localhost

## Next Steps

Once you've tested the basic functionality, you can:
1. Customize the theme in `static/css/style.css`
2. Add new features like file sharing
3. Integrate with a database for persistence
4. Deploy to a cloud platform

Enjoy your new ChatApp! 🎉
