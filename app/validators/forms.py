
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired,Length,Email,Regexp,ValidationError
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form
from app.libs.error_code import ParameterException

# 客户端共有属性验证器(基类),获取客户端传过来的type字段
class ClientForm(Form):
    account = StringField(validators=[DataRequired(message="这个字段是必传参数"),Length(min=5,max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])
    
    #自定义验证器,并转换为枚举类型
    def validate_type(self,value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client
    
# 验证邮件客户端
class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message="invalidate email")])
    secret = StringField(validators=[DataRequired(),Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(),Length(min=2,max=22)])
    
    # 验证用户是否已经存在
    def validate_account(self,value):
        if User.query.filter_by(email=value.data).first():
            raise ParameterException(msg="用户已经存在")
        
        

