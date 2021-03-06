"""Jennifer Meara portfolio website"""

from jinja2 import StrictUndefined
from flask import (Flask, render_template)
from flask_debugtoolbar import DebugToolbarExtension
import os

# Create app
application = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
application.secret_key = os.environ['FLASK_SECRET_KEY']

# If an undefined variable is used in Jinja2, it will raise an error.
application.jinja_env.undefined = StrictUndefined


# this is the route to the homepage
@application.route('/')
@application.route('/index')
def index():
    """Homepage."""
    return render_template("homepage.html")


if __name__ == "__main__":
    application.debug = True

    # make sure templates, etc. are not cached in debug mode
    application.jinja_env.auto_reload = application.debug

    DebugToolbarExtension(application)

    application.run(port=5000, host='0.0.0.0')
