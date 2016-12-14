# -*- coding: utf-8 -*-

import os
import time

import re

from config import GlobalVar
from app import app
from app.utils import file,shell,ssh


from flask import Flask, request, render_template, redirect, url_for, jsonify

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(GlobalVar.BASE_DIR, 'static/uploads')
MESSAGE_PATH=UPLOAD_FOLDER+'/message.txt'


@app.route('/user/register', methods=['POST'])
def register():
    name = request.form.get("name")
    email=request.form.get("email")
    password=request.form.get("password")
    phone=request.form.get("phone")

    name_pattern = re.match("[a-zA-Z0-9 _]*",name)
    if name_pattern is None:
        return jsonify({"code":400,"message": "name formate error"})
    email_pattern = re.match("^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$", email)
    if email_pattern is None:
        return jsonify({"code": 400, "message": "email formate error"})

    user_infos = file.read_from_txt(UPLOAD_FOLDER+'/user_info.txt')
    if user_infos is None:
        file.append_to_txt(UPLOAD_FOLDER + '/user_info.txt', str(request.form.to_dict()) + "\n")
        return jsonify({'code': 200, 'message': 'register succeed!'})
    else:
        return jsonify({'code': 500, 'message': 'error'})
