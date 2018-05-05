import flask
from flask import render_template
from flask import url_for


APP = flask.Flask(__name__)


@APP.route('/')
def route():
        """Redirect the user to the homepage."""
        # return "homepage"
        return flask.render_template('index.html')

if __name__ == '__main__':
   APP.run()