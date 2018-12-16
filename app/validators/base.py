

from wtforms import Form
from app.libs.error_code import ParameterException

# 重写wtforms 加入自己的验证器(未改动父类的validate())
class BaseForm(Form):
    def __init__(self,data):
        # 继承父类的构造函数,同样接受data参数,就是客户端传过来的参数信息(data=request.json)
        super(BaseForm,self).__init__(data=data)

    # form中原有的validate验证器是将错误信息放到errors对象中的,并不会主动抛出来
    # 我们定义一个相同的方法,主动将errors对象中的错误信息给抛出来
    def validate_for_api(self):
        valid = super(BaseForm,self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
    

