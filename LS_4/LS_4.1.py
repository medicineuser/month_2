from types import new_class

class User:

    user_count = 0
    user_password = "123456789"

    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.role = "user"
        self.password = User.user_password
        User.user_count += 1

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @classmethod
    def create_admin(cls,name,phone):
        user = User(name,phone)
        user.role = "admin"
        user.password = "qwerty123"
        return user

    @staticmethod
    def validate_password(pswd):
        if len(pswd) > 8:
            return True
        else:
            return False


    def change_password(self,new_password):
        if User.validate_password(new_password):
            raise ValueError("Password too short!!!")
        self.password = new_password



user = User("Aix",17)
user = User("Aix",17)
user = User("Aix",17)


# создаем админа через сам класс и create admin это метод класса , а не обьекта
admin = User.create_admin("Ratmir","555 99 55 16")
print(admin.get_user_count())
print(User.get_user_count())
User.validate_password("x")
user.validate_password("x")
user.change_password("1111")





