import importlib
from wxpython.Frame import MyFrame
aa = importlib.import_module('wxpython.Frame')
print aa.MyFrame()
assert type(obj.name) is int