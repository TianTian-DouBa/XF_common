from XF_common.XF_LOG_MANAGE import *
from ctypes import cdll, c_bool

class SO():
    def __init__(self):
        so_path = r'.\activiation32.so'
        self.so = cdll.LoadLibrary(so_path)
        add_log(30,'fn:SO.__init__() .so loaded')

    def plot_trend(self):
        pass

    def gen_machine_active(self):
        """generate the machine identity file for activiation"""
        self.so.WriteActiveFile.restype = c_bool
        #self.so.WriteActiveFile.argtypes = [c_bool]
        result = self.so.WriteActiveFile()
        return result

    def valid_key(self):
        self.so.ValidKey.restype = c_bool
        result = self.so.ValidKey()
        return result
