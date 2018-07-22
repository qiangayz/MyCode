
class BaseSaltModule(object):

    def __init__(self,sys_argvs,db_models,settings):
        self.sys_argvs = sys_argvs
        self.db_models = db_models
        self.setting =settings

    def process(self):
        self.fetch_hosts()
        self.config_data_dic = self.get_selected_os_types()

    def get_selected_os_types(self):
        data = {}
        for host in self.host_list:
            data[host.os_type] = []
        print('-->data',data)
        return data

    def fetch_hosts(self):
        print("there fetching host")
        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            host_list = []
            if '-h' in self.sys_argvs:
                host_str_index = self.sys_argvs.index('-h')+1
                if len(self.sys_argvs)  <= host_str_index:
                    exit('host argument must be provide after -h')
                else:
                    host_str = self.sys_argvs[host_str_index]
                    host_str_list = host_str.split(',')
                    host_list += self.db_models.Host.objects.filter(hostname__in = host_str_list )
            if '-g' in self.sys_argvs:
                group_str_index = self.sys_argvs.index('-g')+1
                if len(self.sys_argvs)  <= group_str_index:
                    exit('group argument must be provide after -g')
                else:
                    group_str = self.sys_argvs[group_str_index]
                    group_str_list = group_str.split(',')
                    group_list = self.db_models.HostGroup.objects.filter(name__in = group_str_list )
                    for group in group_list:
                        host_list +=group.host.select_related()
            self.host_list = set(host_list)
            return True
        else:
            print('host [-h] argument or [-g] argument must be provided')

    def syntax_parser(self, section_name, mod_name, mod_data):
        print("-going to parser state data:", section_name, mod_name)
        for state_item in mod_data:
            print("\t", state_item)
            for key, val in state_item.items():
                if hasattr(self, key):
                    state_func = getattr(self, key)
                    state_func(val)
                else:
                    exit("Error:module [%s] has no argument [%s]" % (mod_name, key))

    def require(self,*args,**kwargs):
        pass