# -*- coding: utf-8 -*-

import paramiko
from app.utils import shell

host=shell.HOST
user=shell.USER
password=shell.PASSWORD

def upload_file_by_userpass(filePath):
    paramiko.util.log_to_file('paramiko.log')
    transport = paramiko.Transport((host, 22))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # paramiko.log 上传至服务器/home/wv/paramiko.log
    sftp.put('paramiko.log', filePath)
    transport.close()


def download_file_by_userpass(filePath):
    paramiko.util.log_to_file('paramiko.log')
    transport = paramiko.Transport((host, 22))
    transport.connect(user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # 将remove_path 下载到本地 local_path
    sftp.get(filePath, 'dump.rdb')
    transport.close()


def execute_by_privatekey(private_key,commands):
    paramiko.util.log_to_file('paramiko.log')  # 创建SSH连接日志文件（只保留前一次连接的详细日志，以前的日志会自动被覆盖）
    private_key = paramiko.RSAKey._from_private_key_file('RSAKey.cfg')
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=host, port=22, username=user, key=private_key)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(commands)
    # 获取命令结果
    print stdout.read()
    # 关闭连接
    ssh.close()

def execute_by_userpass(commands):
    paramiko.util.log_to_file('paramiko.log')  # 创建SSH连接日志文件（只保留前一次连接的详细日志，以前的日志会自动被覆盖）
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(commands)
    result = stdout.read()
    ssh.close()
    return result
