FROM python:3.9.20-slim
WORKDIR /usr/src/app
COPY ./bootcamp-flask-chat-rooms/requirements.txt  .  
RUN pip install --no-cache-dir -r requirements.txt
COPY ./bootcamp-flask-chat-rooms .
EXPOSE 5000
CMD [ "python", "./app.py" ]