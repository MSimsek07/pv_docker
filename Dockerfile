# Use an official Python runtime as a parent image
FROM python:3.10.14-slim

# Set environment variable for model path
ENV MODEL_PATH /app/model_efficientnet.h5

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Run the application
CMD ["streamlit", "run", "app.py"]