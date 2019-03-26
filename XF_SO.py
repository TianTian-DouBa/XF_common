from XF_common.XF_LOG_MANAGE import *
from ctypes import cdll, c_bool, c_wchar_p

class SO():
    def __init__(self):
        so_path = r'.\activiation32.so'
        self.so = cdll.LoadLibrary(so_path)
        add_log(30,'fn:SO.__init__() .so loaded')

    def plot_trend(self, start_s, end_s, trends_s, compare, startTime2_s):
        """plot trends
        start_s:<string>
        end_s:<string>
        trends_s:<string>
        compare:<bool> if compare trends
        startTime2_s:<string> e.g. 
        """
        self.so.TrsPlot.restype = c_bool
        self.so.TrsPlot.argtypes = [c_wchar_p,c_wchar_p,c_wchar_p,c_bool, c_wchar_p]
        result = self.so.TrsPlot(start_s, end_s, trends_s, compare, startTime2_s)
        return result

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
