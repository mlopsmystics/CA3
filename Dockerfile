# Use the official Python image as the base image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the specific folder (containing server.py) into the container
COPY flask /app

# Install Flask (if not already installed)
RUN pip install flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "server.py"]
