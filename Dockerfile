# create dockerfile to run myChatGPT.py

FROM python:3.6

# Copy the app folder into the container
COPY app/myChatGPT.py app/requirements.txt /app/

# Set the working directory
WORKDIR /app

# Install the necessary dependencies
RUN pip install -r requirements.txt

# Set the environment variables
ENV ENGINE="text-davinci-003"

# Mount the log folder as a volume
VOLUME app/log

# Run the script
CMD ["python", "myChatGPT.py"]