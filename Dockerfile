FROM python:3.9.20-slim
WORKDIR /usr/src/app
COPY ./python-app/requirements.txt  .  
RUN pip install --no-cache-dir -r requirements.txt
COPY ./python-app . 
EXPOSE 5000
CMD [ "python", "./app.py" ]