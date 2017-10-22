# Start with a Python image.
FROM python:latest

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

# Install some necessary things.
RUN apt-get update
RUN pip install pipenv

# Copy all our files into the image.
RUN mkdir /code
WORKDIR /code

# Install our requirements.
RUN pipenv install --system

# Run command
CMD ["/code/prod.sh"]