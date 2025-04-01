# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /backend
COPY . /app

# Step 4: Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port FastAPI will run on
EXPOSE 8000

# Step 6: Run the FastAPI backend using uvicorn when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
