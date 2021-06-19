from flask import Flask, Response
import json
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

app.run()