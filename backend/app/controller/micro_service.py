# -*- coding: utf-8 -*-

import os
import time

from flask import Response

from config import GlobalVar
from app import app
from app.utils import file,shell,ssh

from flask import Flask, request, render_template, redirect, url_for, jsonify

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(GlobalVar.BASE_DIR, 'static/uploads')
MESSAGE_PATH=UPLOAD_FOLDER+'/message.txt'


@app.route('/service/upload', methods=['GET', 'POST','OPTIONS'])
def upload():
    if request.method == 'GET':

        return render_template('index.html')

    elif request.method == 'POST':

        f = request.files['jarFile']
        if  f.filename == '':
            return Response({"message":"please select a file to upload"},mimetype="application/json")
        fname = secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
        name=request.form.get("name")
        print name
        if name =='':
            return Response({"message": "please input the userId"},mimetype="application/json")
        serviceId=fname+"_"+time.strftime("%Y%m%d%H%M%S",time.localtime())
        upload_message=request.form.to_dict()
        upload_message['fileName']=fname
        upload_message['serviceName']=fname.strip("name")
        upload_message['serviceId']=serviceId
        file.append_to_txt(UPLOAD_FOLDER+'/message.txt',str(upload_message)+"\n")
        f.save(os.path.join(UPLOAD_FOLDER, fname))

        resp = Response({'code':200,'message':'upload succeed!'})
        return resp


@app.route('/service/list', methods=['GET', 'POST'])
def service_list():

    if request.method == 'POST':

        host=request.form.get("host")
        userName=request.form.get("username")
        password=request.form.get("password")
        jarLocation=request.form.get("jarLocation")
        command=request.form.get("command")

        result = ssh.execute_by_userpass('cd '+jarLocation+'\n ls *.jar')
        jars = result.strip("\n").split("\n")
        jar_status={}
        #get there status
        status_result=ssh.execute_by_userpass('ps -ef|grep -E \'' + result.strip("\n").replace("\n","|")+"\'|grep -v grep")
        for jar in jars:
            if jar in status_result:
                jar_status[jar]='up'
            else:
                jar_status[jar]='out_of_service'

        return jsonify({ 'status_result':jar_status})

    elif request.method == 'GET':
        messages = file.read_from_txt(MESSAGE_PATH)
        return jsonify({'services':messages})


@app.route('/service/operate', methods=['POST'])
def service_status():

    if request.method == 'POST':

        host=request.form.get("host")
        userName=request.form.get("username")
        password=request.form.get("password")
        jarLocation=request.form.get("jarLocation")
        command=request.form.get("command")

        if command=='start':
            result = ssh.execute_by_userpass('nohup java -jar '+jarLocation+' >>/dev/null 2>&1 & \n sleep 1 \n ps -ef|grep \'${serviceJarPath}\'|grep -v grep')
            #result deal
            return jsonify({'message':'not implemented!'})
        elif command=='stop':
            result = ssh.execute_by_userpass('ps -ef |grep '+jarLocation+'|grep -v grep|awk \'{print $2}\'|xargs kill -9|ps -ef |grep '+jarLocation+' |grep -v grep')
            #result deal
            return jsonify({'message': 'not implemented!'})
        elif command=='status':
            result = ssh.execute_by_userpass('ps -ef|grep \''+jarLocation+'\'|grep -v grep')
            #result deal
            return jsonify({'message': 'not implemented!'})

    elif request.method == 'GET':

        return jsonify({'message':'not implemented!'})


@app.route('/service/deploy', methods=['POST'])
def service_deploy():

    if request.method == 'POST':

        host=request.form.get("host")
        userName=request.form.get("username")
        password=request.form.get("password")
        jarLocation=request.form.get("jarLocation")
        command=request.form.get("command")

        if command=='start':
            result = ssh.execute_by_userpass('nohup java -jar '+jarLocation+' >>/dev/null 2>&1 & \n sleep 1 \n ps -ef|grep \'${serviceJarPath}\'|grep -v grep')
            #result deal
            return jsonify({'message':'not implemented!'})
        elif command=='stop':
            result = ssh.execute_by_userpass('ps -ef |grep '+jarLocation+'|grep -v grep|awk \'{print $2}\'|xargs kill -9|ps -ef |grep '+jarLocation+' |grep -v grep')
            #result deal
            return jsonify({'message': 'not implemented!'})
        elif command=='status':
            result = ssh.execute_by_userpass('ps -ef|grep \''+jarLocation+'\'|grep -v grep')
            #result deal
            return jsonify({'message': 'not implemented!'})

    elif request.method == 'GET':

        return jsonify({'message':'not implemented!'})


@app.route('/api/service/info', methods=['GET'])
def runing_service_detail():
    resp = Response('[{\"id\":\"123\",\"name\":\"parkme\",\"uploadTime\":\"2016-11-21\",\"description\":\"this is sort description for service\"}]')
    return resp