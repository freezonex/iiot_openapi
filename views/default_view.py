# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import sys
from datetime import datetime
import socket

import flask
from importlib import reload
from os import path

import requests
from flask import current_app, jsonify, make_response, request, g

default_view = flask.Blueprint('default_view', __name__)

basedir = path.realpath(path.join(path.dirname(__file__), '../..'))
sys.path.append(basedir)
reload(sys)


@default_view.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST' or request.method == 'GET':
        current_time = datetime.now()
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        data = {
            "Server Time": current_time,
            "Server IP Address": ip_address
        }
        json_data = {"status_code": 0, "status_message": "success", "data": data}
        return jsonify(json_data)

