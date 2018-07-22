import os,sys
# from Arya import models

if __name__ =='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Stark.settings")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    from Arya.backends.utils import ArgvManagement
    obj = ArgvManagement(sys.argv)