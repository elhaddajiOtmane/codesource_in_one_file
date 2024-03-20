# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Define environment variable
ENV START_PATH="/path/to/your/js/files"
ENV OUTPUT_FILE_PATH="/path/to/output/combined.js"

# Run concatenate_js.py when the container launches
CMD ["python", "./concatenate_js.py"]
