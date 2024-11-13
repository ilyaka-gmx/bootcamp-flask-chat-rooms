from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve static HTML (front end) on GET /
@app.route('/')
def serve_home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)