# Stage 1: Builder
FROM python:3.8-slim-buster AS builder

# Set the working directory inside the container
WORKDIR /app

# Update the package lists and install necessary build tools and libraries
RUN apt-get update && apt-get install -y build-essential libpq-dev gettext && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies into a separate directory
RUN pip install --prefix=/install -r requirements.txt

# Stage 2: Runtime
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Install gettext in the runtime stage
RUN apt-get update && apt-get install -y gettext && rm -rf /var/lib/apt/lists/*

# Copy dependencies from the builder stage into the final image
COPY --from=builder /install /usr/local

# Copy the app's source code into the final image
COPY . .

# Set Python environment variable for unbuffered output
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=edutech.settings


# Expose port 8001
EXPOSE 8000

# Command to run the app with Gunicorn
CMD ["gunicorn", "edutech.wsgi:application", "--bind", "0.0.0.0:8000"]
