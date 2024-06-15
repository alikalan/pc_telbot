FROM python:3.12-slim

WORKDIR app
# Copy the necessary files as the root user
COPY requirements.txt requirements.txt
COPY telegram telegram
COPY utils.py utils.py

# Install Python packages system-wide
RUN pip3 install --no-cache-dir -r requirements.txt

# Set PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Expose the port and start the application
CMD ["python", "telegram/bot.py"]  --host 0.0.0.0 --port $PORT
