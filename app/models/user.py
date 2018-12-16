from sqlalchemy import Column,Integer,String,SmallInteger
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.base import Base,db
from app.libs.error_code import NotFound,AuthFailed


#用户模型
class User(Base):
    id = Column(Integer,primary_key=True)
    email = Column(String(24),unique=True,nullable=False)
    nickname = Column(String(24),unique=True)
    auth = Column(SmallInteger,default=1)
    _password = Column('password',String(100))
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    #给模型定义一个注册用户的方法
    @staticmethod
    def register_by_email(nickname,account,secret):
        with db.auto_commit():
            user = User()
            user.email = account
            user.nickname = nickname
            user.password = secret
            db.session.add(user)
            
    # 验证用户登录(验证成功后返回uid)
    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise NotFound(msg="用户不存在")
        if not user.check_password(password):
            raise AuthFailed()
        return {"uid":user.id}

        
    # 定义一个验证密码的函数
    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password,raw)
        

    