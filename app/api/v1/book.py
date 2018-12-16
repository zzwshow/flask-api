


from app.libs.redprint import Redprint

# redprint

# 创建红图对象,并传入此红图要使用的的url前缀
api = Redprint("book")



@api.route("",methods=["GET"])
def get_book():
    return "get book"


@api.route("",methods=["POST"])
def create_book():
    return "create book"