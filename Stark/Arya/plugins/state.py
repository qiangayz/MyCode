import os
from Arya.backends.base_module import BaseSaltModule


class State(BaseSaltModule):

    def load_state_files(self, state_filename):
        from yaml import load, dump
        try:
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper
        state_file_path = "%s/%s" % (self.setting.SALT_CONFIG_FILES_DIR, state_filename)
        if os.path.isfile(state_file_path):
            with open(state_file_path) as f:
                data = load(f.read(), Loader=Loader)
                return data
        else:
            exit("%s is not a valid yaml config file" % state_filename)


    def apply(self):
        """
        1、下载配置文件
        2、解析
        3、创建一个任务，并发送到队列
        4、收集任务结果
        :return:
        """
        if '-f' in self.sys_argvs:
            yaml_file_index = self.sys_argvs.index('-f') + 1
            try:
                yaml_filename = self.sys_argvs[yaml_file_index]
                state_data = self.load_state_files(yaml_filename)
                for os_type, os_type_data in self.config_data_dic.items():  # 按照不同的操作系统单独生成一份配置文件
                    for section_name, section_data in state_data.items():
                            print('Section:', section_name)
                            for mod_name, mod_data in section_data.items():
                                base_mod_name = mod_name.split(".")[0]
                                plugin_file_path = "%s/%s.py" % (self.setting.SALT_PLUGINS_DIR, base_mod_name)
                                if os.path.isfile(plugin_file_path):
                                    module_plugin = __import__('plugins.%s' % base_mod_name)
                                    special_os_module_name = "%s%s" % (os_type.capitalize(), base_mod_name.capitalize())
                                    getattr(module_plugin, base_mod_name)
                                    module_file = getattr(module_plugin, base_mod_name)
                                    if hasattr(module_file, special_os_module_name):  # 判断有没有根据操作系统的类型进行特殊解析 的类，在这个文件里
                                        module_instance = getattr(module_file, special_os_module_name)
                                    else:
                                        module_instance = getattr(module_file, base_mod_name.capitalize())
                                    module_obj = module_instance(self.sys_argvs, self.db_models, self.setting)
                                    module_obj.syntax_parser(section_name, mod_name, mod_data)
                                else:
                                    exit("module [%s] is not exist" % base_mod_name)
                                print(" ",mod_name)
                                for state_item in mod_data:
                                    print("\t",state_item)
                            # base_mod_name = mod_name.split(".")[0]
                            # plugin_file_path = "%s/%s.py" % (self.setting.SALT_PLUGINS_DIR, base_mod_name)
                            # if os.path.isfile(plugin_file_path):
                            #     # 导入 模块
                            #
                            #     module_plugin = __import__('plugins.%s' % base_mod_name)
                            #     special_os_module_name = "%s%s" % (os_type.capitalize(), base_mod_name.capitalize())
                            #     # print('dir module plugin:',module_plugin,base_mod_name)
                            #     # getattr(module_plugin,base_mod_name)
                            #     module_file = getattr(module_plugin, base_mod_name)  # 这里才是真正导入模块
                            #     if hasattr(module_file, special_os_module_name):  # 判断有没有根据操作系统的类型进行特殊解析 的类，在这个文件里
                            #         module_instance = getattr(module_file, special_os_module_name)
                            #     else:
                            #         module_instance = getattr(module_file, base_mod_name.capitalize())
                            #
                            #     # 开始调用 此module 进行配置解析
                            #     module_obj = module_instance(self.sys_argvs, self.db_models, self.settings)
                            #     module_obj.syntax_parser(section_name, mod_name, mod_data)
                            # else:
                            #     exit("module [%s] is not exist" % base_mod_name)
                            #     # print("  ",mod_name)
                            #     # for state_item in mod_data:
                            #     #    print("\t",state_item)

            except IndexError as e:
                exit("state file must be provided after -f")

        else:
            exit("statefile must be specified.")