
from flask import current_app,jsonify
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint("token")

# 获取token(验证用户的用户名和密码)
@api.route('', methods = ["POST"])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify, #100:User.verify
    }
    
    # 根据用户提交上来的type类型获取promise中对应的验证方法!
    # "ClientTypeEnum(form.type.data)" = ClientTypeEnum.USER_EMAIL 将客户端传来的type值转换为枚举类名!
    identify = promise[ClientTypeEnum(form.type.data)](form.account.data,form.secret.data)
    # Token
    expiration = current_app.config["TOKEN_EXPIRATION"]
    token = generate_auth_token(identify["uid"],
                                ac_type=form.type.data,
                                scope=None,
                                expiration=expiration)
    # 需要给客户端返回json数据,需要讲byte类型的token进项转换
    t = {
        "token": token.decode('ascii')
    }
    return jsonify(t),201
    
    
    pass


# 生成令牌 token
def generate_auth_token(uid,ac_type,scope=None,expiration=7200):
    '''token包含三个信息:
        1 用户uid
        2 客户端类型
        3 权限 (暂时先不实现)
    '''
    # Serializer生成令牌
    s = Serializer(current_app.config["SECRET_KEY"],
                   expires_in=expiration)
    
    # 调用令牌对象的dumps方法将我们要加入令牌的信息添加进去(return 返回的是一个byte类型的字符串!)
    return s.dumps({
        'uid':uid,
        'type':ac_type.value
    })
    
    