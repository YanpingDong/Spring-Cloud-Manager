# -*- coding: utf-8 -*-
from app.utils.Properties import Properties
from app import app
from config import GlobalVar

if __name__ == '__main__':
    properties = Properties(GlobalVar.BASE_DIR + '/config.properties')
    app.debug = properties.get('debug')           # 设置调试模式，生产模式的时候要关掉debug
    app.run(host=properties.get('host'))                  # 启动服务器