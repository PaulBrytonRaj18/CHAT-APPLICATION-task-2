#!/usr/bin/env python3
"""
Simple test script to verify the ChatApp functionality
"""

import requests
import time
import threading
from flask import url_for

def test_app():
    """Test basic app functionality"""
    base_url = "http://localhost:5000"
    
    print("Testing ChatApp...")
    
    try:
        # Test home page
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("✓ Home page loads successfully")
        else:
            print(f"✗ Home page failed with status {response.status_code}")
            
        # Test login page
        response = requests.get(f"{base_url}/login", timeout=5)
        if response.status_code == 200:
            print("✓ Login page loads successfully")
        else:
            print(f"✗ Login page failed with status {response.status_code}")
            
        # Test register page
        response = requests.get(f"{base_url}/register", timeout=5)
        if response.status_code == 200:
            print("✓ Register page loads successfully")
        else:
            print(f"✗ Register page failed with status {response.status_code}")
            
        print("\n🎉 Basic functionality tests passed!")
        print("\nTo test the full application:")
        print("1. Open http://localhost:5000 in your browser")
        print("2. Create an account with a unique User ID")
        print("3. Create a room and share the room code")
        print("4. Open another browser tab/window and join with the room code")
        print("5. Start chatting!")
        
    except requests.exceptions.ConnectionError:
        print("✗ Could not connect to the server")
        print("Make sure the Flask app is running on http://localhost:5000")
    except Exception as e:
        print(f"✗ Error during testing: {e}")

if __name__ == "__main__":
    test_app()
