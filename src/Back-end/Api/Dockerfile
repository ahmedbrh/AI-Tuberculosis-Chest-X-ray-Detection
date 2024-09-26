# Step 1: Use the official Python image from Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt /app/


# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the current directory contents into the container
COPY . /app/

# Step 6: Expose port 8000 (FastAPI default port)
EXPOSE 8000

# Step 7: Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]