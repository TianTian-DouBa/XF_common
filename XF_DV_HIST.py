from subprocess import run, Popen
from XF_common.XF_LOG_MANAGE import *
#from XF_common.XF_XML import

EXE_PATH = r"C:\DeltaV\bin\OPCHDAClient.exe"

def execute_xml(xml_path):
    """execute the xml by OPCHDAClient.exe"""
    run([EXE_PATH,xml_path])

def valid_value(value):
    """valid the value:
    -return:<string> 'none' or 'Batch_ID'
    -value:<string>
    """
    if isinstance(value,str):
        _strip = value.strip()
        _value = _strip.lower()
        if _value == 'none' or _value == '':
            return 'none'
        else:
            return _strip
    else:
        return 'none'

if __name__ == '__main__':
    a = "  none"
    print(a,':' ,valid_value(a))
    a = "    "
    print(a,':' ,valid_value(a))
    a = " asdfasdf "
    print(a,':' ,valid_value(a))
    a = "NONE"
    print(a,':' ,valid_value(a))
    xml_path = r'.\XF_XML_sub\OpcHdaTST001.xml'
    execute_xml(xml_path)
    Popen(["notepad", r".\XF_XML_sub\sim-001.csv"])
