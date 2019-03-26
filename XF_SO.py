from XF_common.XF_LOG_MANAGE import *
from ctypes import cdll, c_bool

so = None #.so包

def init_so():
    """initialize .so file located in main.py folder"""
    global so
    so = cdll.LoadLibrary(r'.\activiation32.so')
    add_log(30,'fn:init_so() loaded')

def plot_trend():
    pass

def valid_key():
    so.ValidKey.restype = c_bool
    result = so.ValidKey()
    return result
