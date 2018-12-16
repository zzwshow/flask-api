
from werkzeug.exceptions import HTTPException
from app.libs.error import APIException


class ClientTypeError(APIException):
    # http 响应状态码
    code = 400
    # 错误提示内容
    msg = "客户端类型错误..."
    # 错误代码
    error_code = 1006


# 定义一个通用的参数异常信息
class ParameterException(APIException):
    code = 400
    msg = ''
    error_code = 1000

