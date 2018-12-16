from app.libs.redprint import Redprint
from app.validators.forms import ClientForm,UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.models.user import User

api = Redprint("client")

@api.route("/register",methods=["POST"])
def create_client():
    #data = request.json #获取客户端json提交的数据
    ##form = ClientForm() #在BaseForm中我们已经将data传进去了
    ##使用我们自己定义的验证器,验证不通过就会抛出异常信息(下面代码就不会执行了)
    ##form.validate_for_api()
    # 参数验证通过后下面代码会根据参数中的type类型,执行不同的验证逻辑
    
    # 合并上面两行代码(前提是validate_for_api()要返回实例本身这里就是"ClientForm()"然后赋值给form变量)
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL:__register_user_by_email
    }
    # 从验证器拿到客户端类型,然后调用该类型的验证器进行验证
    promise[form.type.data]()
    return Success()
    
    # 客户端提交数据方式  1 表单  2 json
    # 服务端接收方式: 1 request.json   2 request.args.to_dict()
    # 注册 登录
    # 参数 效验 接收参数
    # WTForms 验证表单

#为不同的客户端创建不同的注册逻辑(使用email注册的用户处理逻辑)
def __register_user_by_email():
    form =  UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,form.account.data,form.secret.data)
        
def __register_user_by_wx():
    pass

