import sys
import django
django.setup()
from Stark import settings
from Arya import action_list
from Arya import models


class ArgvManagement(object):
    """
    接受用户从命令行输入的指令，并分配到相应的模块
    """
    def __init__(self,argvs):
        self.argvs = argvs
        self.argv_parse()

    def help_msg(self):
        print("Available modules:")
        for registered_module in action_list.actions:
            print(" %s" % registered_module)
        exit()

    def argv_parse(self):
        if len(self.argvs) < 2:
            self.help_msg()
        module_name = self.argvs[1]
        if "." in module_name:
            mod_name,mod_method = module_name.split('.')
            module_instance = action_list.actions.get(mod_name)
            if module_instance:
                module_obj = module_instance(self.argvs,models,settings)
                module_obj.process() #解析任务，发送到队列，取任务结果
                if hasattr(module_obj,mod_method):
                    module_method_obj = getattr(module_obj,mod_method)
                    module_method_obj()#调用指定的指令
                else:
                    exit("module [%s] doesn't have [%s] method" % (mod_name,mod_method))
        else:
            exit('invalid module name argument')