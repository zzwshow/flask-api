from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError
from werkzeug.exceptions import HTTPException



app = create_app()

# #异常梳理 (捕捉所有异常统一返回标准json格式!)
# 已知异常  我们可以使用自己定义的APIException
# 未知异常  flask 框架还是会返回非json的错误提示

# 这个装饰器可以捕捉到整个项目的所有异常(flask1.0 以下版本不能使用,没有Exception基类)
# flask1.0 以下版本只能捕捉到特定的异常信息
@app.errorhandler(Exception)
def framework_error(e):
    # 异常分类
    # 1 APIException (也就是我们定义的标准json异常(已知异常))
    # 2 HTTPException (http请求的其他异常,(未知异常))
    # 3 Exception (python 原生异常)
    
    if isinstance(e,APIException):
        return e
    if isinstance(e,HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007 # 自定义错误代码(表示HTTPException的未知异常)
        return APIException(code,msg,error_code)
    else:
        # python原生的基类异常 就不要返回给前端了.后台记录日志!!
        # 返回APIException() 默认的未知异常即可
        
        if not app.config["DEBUG"]:
        # 在调试中我们还是希望可以看到具体的错误信息的,在返回默认错误提示显然不方便调试
            return ServerError()
        else:
            raise e
if __name__ == "__main__":
    app.run(debug=True)
