import flask
from flask import Flask, send_from_directory, send_file, request, Response
from datetime import datetime
import os

app = Flask(__name__)

# Ensure chat directory exists
CHAT_DIR = os.path.join(os.getcwd(), 'chat')
os.makedirs(CHAT_DIR, exist_ok=True)
app = Flask(__name__)

# Serve static HTML (front end) on GET /
# Shai
@app.route('/')
def serve_home():
    return send_from_directory('.', 'index.html')

# Ilya 
@app.route('/<room>')
def serve_page(room):
    return send_file('index.html')

# Ilya
@app.route('/api/chat/<room>', methods=['POST'])
def post_message(room):
    username = request.form.get('username')
    message = request.form.get('msg')
    
    if not username:
        return "Username is required", 400

    if not message:
        return "Message is required", 400
    
    # Format the message with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_message = f"[{timestamp}] {username}: {message}\n"
    
    # Create and write to room-specific file
    filename = os.path.join(CHAT_DIR, f'messages_{room}.txt')
    
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(formatted_message)
        return "Message sent successfully", 200
    except Exception as e:
        return f"Error saving message: {str(e)}", 500
    
# Shai
@app.route('/api/chat/<room>', methods=['GET'])
def get_messages(room):
    filename = os.path.join(CHAT_DIR, f'messages_{room}.txt')
    
    try:
        if not os.path.exists(filename):
            return ""
        
        with open(filename, 'r', encoding='utf-8') as f:
            messages = f.read()
        return Response(messages, mimetype='text/plain')
    except Exception as e:
        return f"Error reading messages: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
