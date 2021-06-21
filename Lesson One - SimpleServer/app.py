# These are our imports! They help us avoid writing boring low-level code
from flask import Flask, Response
import json

# Here we create our app object so that we have somewhere
# to place all our pages and endpoints
app = Flask(__name__)

# Our very first endpoint/page: A simple hello world
# Note the annotation. The argument provided will determine what the web address is.
@app.route("/")
def index():
    # First we need to open our html file
    f = open("index.html")
    # and read it into a new variable.
    resp_content = f.read()

    # Next we create our response and make sure we add headers
    # so that the Content-Type matches the data we've provided
    resp = Response(resp_content, headers={'Content-Type': 'text/html'})

    # Finally, we return our response.
    return resp

# Here's where we start our little web server!
if __name__ == '__main__':
    app.run()