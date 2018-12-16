from flask import Blueprint
from app.api.v1 import book,user,client


# 定义一个〔v1〕蓝图
def create_blueprint_v1():
    bp_v1 = Blueprint("v1",__name__)
    user.api.register(bp_v1)  #将红图注册到蓝图中
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    
    return bp_v1

    


