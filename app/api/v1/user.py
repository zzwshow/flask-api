

from app.libs.redprint import Redprint


api = Redprint("user")



@api.route("",methods = ["GET"])
def get_user():
    return "get user"

@api.route("", methods=["POST"])
def create_user():
    # name
    # password
    # 数据
    # 第三方 自己的产品 APP 小程序 用户
    # 人
    # 客户端 client
    # 种类非常多
    # 出册的形式非常多 短信 邮件 QQ 微信
    return "create user"

@api.route("",methods = ["PUT"])
def update_user():
    return "update user"

@api.route("",methods = ["DELETE"])
def delete_user():
    return "delete user"