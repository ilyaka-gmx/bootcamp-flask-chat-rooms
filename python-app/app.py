import flask
from flask import Flask, send_from_directory, send_file, request, Response
from datetime import datetime
import os
import MySQLdb

def wait_for_db(max_retries=30, delay=2):
    for attempt in range(max_retries):
        try:
            conn = get_db_connection()
            conn.close()
            print("Successfully connected to database")
            return True
        except MySQLdb.Error as e:
            print(f"Database connection attempt {attempt + 1} failed. Retrying in {delay} seconds...")
            time.sleep(delay)
    return False


app = Flask(__name__)

# MySQL Database Configuration
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', 'chatrooms')

def get_db_connection():
    return MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

def init_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create messages table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        room VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()

# Initialize database on app startup
if wait_for_db():
    init_database()
else:
    print("Failed to connect to database after maximum retries")

# Serve static HTML (front end) on GET /
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
    
    # Insert message into MySQL database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO messages (room, username, message) VALUES (%s, %s, %s)", 
            (room, username, message)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return "Message sent successfully", 200
    except Exception as e:
        conn.rollback()
        return f"Error saving message: {str(e)}", 500
    
# Shai
@app.route('/api/chat/<room>', methods=['GET'])
def get_messages(room):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Retrieve messages for specific room
        cursor.execute(
            "SELECT timestamp, username, message FROM messages WHERE room = %s ORDER BY timestamp", 
            (room,)
        )
        
        # Format messages like the original text file output
        messages = []
        for row in cursor.fetchall():
            timestamp, username, message = row
            formatted_message = f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {username}: {message}\n"
            messages.append(formatted_message)
        
        cursor.close()
        conn.close()
        
        return Response(''.join(messages), mimetype='text/plain')
    except Exception as e:
        return f"Error reading messages: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)