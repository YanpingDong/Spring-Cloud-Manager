
# -*- coding: utf-8 -*-

import os
from config import GlobalVar
from app import app
from app.utils import file

from flask import Flask, request, render_template, redirect, url_for, jsonify

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(GlobalVar.BASE_DIR, 'static/uploads')

@app.route('/message/get', methods=['GET'])
def message_get():
        messages = file.read_from_txt(UPLOAD_FOLDER+'/message.txt')
        print(messages)

        return jsonify({'messages':messages})


