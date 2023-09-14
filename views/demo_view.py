# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

import flask
from importlib import reload
from os import path
from flask import request, jsonify, g, make_response

from utils.demo_utils import *

demo_view = flask.Blueprint('demoview', __name__)
basedir = path.realpath(path.join(path.dirname(__file__), '../..'))
sys.path.append(basedir)
reload(sys)


@demo_view.route('/api/demo/air-quality/get', methods=['GET'])
def get_demo_air_quality_fun():
    method_name = get_demo_air_quality_fun.__name__
    try:
        req_body = request.args.to_dict()
        if 'node_id' in req_body:
            node_id = req_body["node_id"]
        else:
            node_id = None
        if 'node_num' in req_body:
            node_num = int(req_body["node_num"])
        else:
            node_num = None
        rsp = get_demo_air_quality(node_id=node_id, node_num=node_num)
        json_data = {"status_code": 200, "status_message": "success", "data": rsp}
        return jsonify(json_data)
    except Exception:
        msg = method_name + " exception, " + traceback.format_exc()
        json_data = {"status_code": 400, "status_message": msg, "data": None}
        return jsonify(json_data)


@demo_view.route('/api/demo/water-meter/get', methods=['GET'])
def get_demo_water_meter_fun():
    method_name = get_demo_water_meter_fun.__name__
    try:
        req_body = request.args.to_dict()
        if 'node_id' in req_body:
            node_id = req_body["node_id"]
        else:
            node_id = None
        if 'node_num' in req_body:
            node_num = int(req_body["node_num"])
        else:
            node_num = None
        rsp = get_demo_water_meter(node_id=node_id, node_num=node_num)
        json_data = {"status_code": 200, "status_message": "success", "data": rsp}
        return jsonify(json_data)
    except Exception:
        msg = method_name + " exception, " + traceback.format_exc()
        json_data = {"status_code": 400, "status_message": msg, "data": None}
        return jsonify(json_data)