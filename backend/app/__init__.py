# -*- coding: utf-8 -*-

from flask import Flask        # 引入 flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask_cors import CORS
from config import GlobalVar

app = Flask(__name__, template_folder=GlobalVar.BASE_DIR + '/templates')          # 实例化一个flask 对象
CORS(app)

from app.controller import micro_service,message,system,user
# from app import views


@app.route('/')
def index():

    return render_template('index.html')