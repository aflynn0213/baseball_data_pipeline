# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY ../requirements.txt ./  # Adjusted path to requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY .. .  # Adjusted path to copy project files

# Expose port for Dash app
EXPOSE 8050

# Command to run the Dash app
CMD ["python", "app.py"]
