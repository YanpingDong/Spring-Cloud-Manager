import os

from flask import Flask, request, render_template, redirect, url_for, jsonify
from app import app

from app.utils import ssh
from config import GlobalVar

UPLOAD_FOLDER = os.path.join(GlobalVar.BASE_DIR, 'static/uploads')


@app.route('/system/top', methods=['POST'])
def top():
    host=request.form.get("host")
    userName=request.form.get("username")
    password=request.form.get("password")
    jarLocation=request.form.get("jarLocation")

    top_result = ssh.execute_by_userpass('top -b -n 1')

    [summary,items]=top_result.split("\n\n")
    [top,tasks,cpu,mem,swap]=summary.split("\n")

    print(tasks)
    print(cpu)
    print(mem)
    print(swap)
    print(items)

    response={}
    response['loadAverage']=top.split(",  ")[-1].split(":")[-1]
    response['tasks'] = {}
    for element in tasks.split(":")[-1].split(","):
        response['tasks'][element.strip(" ").split(" ")[-1]] = element.strip(" ").split(" ")[0]

    response['mem'] = {}
    for element in mem.split(":")[-1].split(","):
        response['mem'][element.strip(" ").split(" ")[-1]]=element.strip(" ").split(" ")[0]

    response['cpu'] = {}
    for element in cpu.split(":")[-1].split(","):
        response['cpu'][element.strip(" ").split(" ")[-1]] = element.strip(" ").split(" ")[0]

    response['swap'] = {}
    for element in swap.split(":")[-1].split(","):
        response['swap'][element.strip(" ").split(" ")[-1]] = element.strip(" ").split(" ")[0]

    disk_result = ssh.execute_by_userpass('df -lh')
    disk_list=disk_result.split("\n")
    disk_list.pop(0)
    disk_return=[]
    for element in disk_list:
        if element != '':
            [file_system, size, used, avail, use_persent, mounted_on] = element.split()
            disk_return.append({'file_system':file_system,'size':size,'used':used,'avail':avail,'use_persent':use_persent,'mounted_on':mounted_on})


    response['disk']=disk_return
    return jsonify(response)

