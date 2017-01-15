# -*- coding: utf-8 -*-
from app import app
from config import GlobalVar

if __name__ == '__main__':
    app.debug = GlobalVar.PROPERTIES.get('debug')           # 设置调试模式，生产模式的时候要关掉debug
    app.run(host=GlobalVar.PROPERTIES.get('host'))                  # 启动服务器