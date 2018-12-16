

from wtforms import Form
from flask import request
from app.libs.error_code import ParameterException

# 重写wtforms 加入自己的验证器(未改动父类的validate())
class BaseForm(Form):
    def __init__(self):
        # 由于data =request.json之前是在视图函数中获取,我们可以在可以定义好,在视图函数中就不需要在传data了
        data = request.json
        # 继承父类的构造函数,同样接受data参数,就是客户端传过来的参数信息(data=request.json)
        super(BaseForm,self).__init__(data=data)

    # form中原有的validate验证器是将错误信息放到errors对象中的,并不会主动抛出来
    # 我们定义一个相同的方法,主动将errors对象中的错误信息给抛出来
    def validate_for_api(self):
        valid = super(BaseForm,self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        # 为了在视图函数中直接使用
        return self

