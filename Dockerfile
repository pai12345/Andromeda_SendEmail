# Python base image
FROM python:alpine as builder

# ENV SENDER_ADDRESS=chessautomationtools@gmail.com
# ENV SENDER_PASS=Test
# ENV RECEIVER_ADDRESS=chessautomationtools@gmail.com
# ENV SMTP_PORT=587


# Create working directory
WORKDIR /app

# Copy contents to app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Execute App
CMD python index.py

