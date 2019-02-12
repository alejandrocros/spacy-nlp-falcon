# Download base image ubuntu 16.04
FROM python:3.6

# Copy files
COPY . ./app

# Set Workdir
WORKDIR /app

# Install requirements
RUN pip3 install -r requirements.txt

# Download model
RUN python -m spacy download pt_core_news_sm

# Define Ports
ENV PORT 9000
EXPOSE $PORT

# Initialize listening (language may be changed)
CMD gunicorn -b 0.0.0.0:9000 'app:main(language="pt")'