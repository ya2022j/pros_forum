#! -*- coding:utf-8 -*-
import os

from flask_cors import cross_origin,CORS


from flask import Flask

app = Flask(__name__)



@app.route("/")
@cross_origin()
def top_homepage():
    return "test nginx port 4567"


if __name__ == '__main__':
    app.run(debug=True,port=4567)



# #CentOS开放指定端口：
# 方式一
#
# 1、开启防火墙
# systemctl start firewalld
#
# 2、开放指定端口
# firewall-cmd --zone=public --add-port=1935/tcp --permanent
# 命令含义：
# –zone #作用域
# –add-port=1935/tcp#添加端口，格式为：端口/通讯协议
# –permanent#永久生效，没有此参数重启后失效
#
# 3、重启防火墙
# firewall-cmd --reload
#
# 4、查看端口号
# netstat -ntlp//查看当前所有tcp端口·
