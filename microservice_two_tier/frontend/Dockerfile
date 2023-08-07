# Use a slim Python image as the base image
FROM python:3.9-slim 

# Set the working directory in the container
WORKDIR /app

# Install Flask and requests
RUN pip install Flask requests

# Copy all necessary files into the container
COPY frontend.py /app/
COPY templates /app/templates

# Expose port 80 to access the Flask app
EXPOSE 80

# Start the frontend Flask app
CMD ["python", "frontend.py"]

