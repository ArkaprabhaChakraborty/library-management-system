# base image
FROM python:3.9.10

#maintainer
LABEL Author="Aniruddha"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED=1

#switch to /lms directory so that everything runs from here
WORKDIR /lms

#copy the app code to image working directory
COPY . .

#let pip install required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
