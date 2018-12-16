
from werkzeug.exceptions import HTTPException
from app.libs.error import APIException

# 定义一个正确的返回值(之所以定义在这里面是因为我们为了使用APIException返回固定的json数据!)
# 在APIException我们已经修改了我们使用的标准返回格式!
class Success(APIException):
    code = 201
    msg = "ok"
    error_code = 0


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

