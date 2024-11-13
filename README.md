

# bootcamp-flask-chat-rooms

A Flask-based real-time chat application with MySQL database support running in Docker containers.

# Features

- Multiple chat rooms support
- Real-time message updates
- Message persistence using MySQL
- Clean and responsive design
- Containerized deployment

# Technologies Used

- Python 3.9
- Flask
- MySQL 8.0
- Docker
- Docker Compose
- HTML/CSS
- JavaScript

# Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bootcamp-flask-chat-rooms.git
```

2. Make sure you have Docker and Docker Compose installed on your system

3. Navigate to the project directory:
```bash
cd bootcamp-flask-chat-rooms
```

4. Build and run the containers:
```bash
docker-compose build
```

5. Verify the images were created:
```bash
docker images
```

6. Start the containers:
```bash
docker-compose up
```

To run containers in detached mode (background):
```bash
docker-compose up -d
```

7. Verify the containers are running:
```bash
docker ps
# or for more detailed view
docker-compose ps
```

8. Access the application at:
```
http://localhost:5000
```

**Note**: To stop the containers when running in detached mode, use:
```bash
docker-compose down
```

# Environment Variables

The following environment variables are configured in docker-compose.yml:

- DB_HOST=db
- DB_USER=root
- DB_PASSWORD=mysecretpassword
- DB_NAME=chatrooms

# Docker Services

The application runs two containers:
- Web service (Flask application)
- MySQL database

# Development

To make changes to the application:

1. Modify the code in python-app directory
2. Rebuild the containers:
```bash
docker-compose down
docker-compose build
docker-compose up
```

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.