# 1. Use an official Python runtime as a parent image
FROM python:3.12-slim

# 2. Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set working directory inside the container
WORKDIR /code

# 4. Install system dependencies (needed for psycopg2)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements file first to leverage Docker cache
COPY requirements.txt /code/

# 6. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 7. Copy the rest of the project code
COPY . /code/

# 8. Expose port 8000 (default Django port)
EXPOSE 8000

# 9. Default command to run your Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
