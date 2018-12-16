from enum import Enum
# 定义请求客户端的类型
class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    
    #微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
    

