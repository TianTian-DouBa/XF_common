from XF_common.XF_LOG_MANAGE import *
from ctypes import cdll, c_bool, c_wchar_p, c_char_p

class SO():
    def __init__(self):
        so_path = r'.\activiation32.so'
        self.so = cdll.LoadLibrary(so_path)
        add_log(30,'fn:SO.__init__() .so loaded')

    def plot_trend(self, start_s, end_s, trends_s, compare, startTime2_s):
        """plot trends
        start_s:<string> e.g.: r'2018/11/03 10:12:00'
        end_s:<string> e.g.: r'2018/11/03 10:50:00'
        trends_s:<string> e.g.: r"SIM-001/SIN.CV, SIM-001/RAMP.CV, , , V1-COMMON/BATCH_ID.CV"
        compare:<bool> if compare trends
        startTime2_s:<string> e.g.: r'2018/11/09 20:31:00'
        """
        self.so.TrsPlot.restype = c_bool
        self.so.TrsPlot.argtypes = [c_char_p,c_char_p,c_char_p,c_bool, c_char_p]
        result = self.so.TrsPlot(str.encode(start_s), str.encode(end_s), str.encode(trends_s), compare, str.encode(startTime2_s))
        return result

    def gen_machine_active(self):
        """generate the machine identity file for activiation"""
        self.so.WriteActiveFile.restype = c_bool
        #self.so.WriteActiveFile.argtypes = [c_bool]
        result = self.so.WriteActiveFile()
        return result

    def valid_key(self):
        """to validate if the activiation key file .\ActiveKey.dt is available
        """ 
        self.so.ValidKey.restype = c_bool
        result = self.so.ValidKey()
        return result
