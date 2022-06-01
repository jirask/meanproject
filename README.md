# meanproject


This is a basic django application that runs an online mean algorithm.
The user sends numerical values to the web-server in a JSON format (it can be a single value or a list containing multiple numbers). The web-server updates its internal state according to the received values, if everything is ok, the user receives a JSON saying that everything went ok, otherwise they receive a JSON error.
The user can ask the web-server for its current internal mean value
The user can also reset the internal state of the web-server.

## Installation

Install the required dependencies:

    pip install -r requirements.txt

Apply migrations:

    python manage.py migrate

Start the django application:

    python manage.py runserver


That's it!

Browse to http://127.0.0.1:8000 to see the editor in action.
