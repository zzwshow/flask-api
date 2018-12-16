

from werkzeug.exceptions import HTTPException
from flask import request,json

# 重写HTTPException 基类使它返回json格式的错误信息
class APIException(HTTPException):
    # 默认值
    code = 500
    msg = "sorry, we make a mistake (~ _ ~)"
    error_code = 999
    
    # 定义构造函数实例化时用来改变默认值
    def __init__(self,code=None,msg=None,error_code=None,headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        # 调用基类的构造函数
        super(APIException,self).__init__(description=msg, response=None)
        
    # 重写get_body方法,让它返回json的数据格式
    def get_body(self, environ=None):
        body = dict(
            msg = self.msg,
            error_code = self.error_code,
            request = request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text
    
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]
    
    
    # 静态方法获取请求url的主路径
    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split("?")
        return main_path[0]
        
