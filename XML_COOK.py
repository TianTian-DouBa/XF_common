import xml.etree.cElementTree as et
from subprocess import run
from LOG_MANAGE import *

def load_xml(path):
    """加载xml文件，返回et.ElementTree对象
    -path: 存放XML文件的路径"""
    try:
        tree = et.ElementTree(file=path)
        return tree
    except FileNotFoundError:
        log_args = [path]
        add_log(10, 'file not found. --"{0[0]}"', log_args)



