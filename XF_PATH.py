import os
import glob
import re
from XF_common.XF_LOG_MANAGE import *

RESULT_STATUS = ('Normal','Path Invalid','Extension Invalid')

def list_file_names(path, extension = None):
    """返回指定路径下，符合表达式的文件名
    -path: <str> 'D:\DeltaV\DVData\CHRONICLE'
    -extension: <str> '.mdf'"""
    if not os.path.exists(path):
        result_status = RESULT_STATUS[1] #Path Invalid
        result = None
        log_args = [path]
        add_log(40, 'fn:list_file_names(); path invalid: {0[0]}', log_args)
        return (result_status,result)
    if extension == None:
        _extension = r'.*'
    elif isinstance(extension, str):
        re_pattern = re.compile(r'^\.(\w)+')
        re_match = re_pattern.match(extension)
        if re_match:
            _extension = extension
        else:
            log_args = [extension]
            add_log(40, 'fn:list_file_names(); extension invalid: {0[0]}', log_args)
            result = None
            result_status = RESULT_STATUS[2] #Extension Invalid
            return (result_status,result)
    _path = path + '\\*' + _extension
    log_args = [_path]
    add_log(40, 'fn:list_file_names(); _path: {0[0]}', log_args)
    result = glob.glob(_path)
    result_status = RESULT_STATUS[0] #Normal
    log_args = [result_status]
    add_log(40, 'fn:list_file_names(); result: {0[0]}', log_args)
    if logable(40):
        for i in result:
            log_print(i)
    return (result_status, result)
