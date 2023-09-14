# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import flask

from views.default_view import default_view
from views.demo_view import demo_view

app = flask.Flask(__name__)

app.register_blueprint(default_view)
app.register_blueprint(demo_view)


if __name__ == '__main__':
    # start flask program
    # Never run this in production environment!
    app.run(host='0.0.0.0', port=5055, threaded=True)