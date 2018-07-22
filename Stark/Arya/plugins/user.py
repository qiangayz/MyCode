
from Arya.backends.base_module import BaseSaltModule

class User(BaseSaltModule):

    def uid(self,*args):
        pass

    def gid(self,*args):
        pass

    def shell(self,*args):
        pass

    def home(self,*args):
        pass

class UbuntuUser(User):
    def home(self,*args):
        print('in ubuntu ')