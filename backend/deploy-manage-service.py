# -*- coding: utf-8 -*-

from app import app          

if __name__ == '__main__':
    app.debug = True           # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='10.120.137.175')                  # 启动服务器