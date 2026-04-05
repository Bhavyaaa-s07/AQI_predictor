# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install streamlit pandas scikit-learn numpy

# Expose the dashboard port
EXPOSE 5050

# Command to run Streamlit on port 5050
CMD ["streamlit", "run", "app.py", "--server.port=5050", "--server.address=0.0.0.0"]