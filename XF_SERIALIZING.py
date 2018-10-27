import pickle
import sys
from XF_common.XF_LOG_MANAGE import add_log, logable

def serializing (obj, file):
    """对象线性化
    -obj: object to serializing
    -file: file path as string"""
    with open(file, "wb") as f:
        pickle.dump(obj, f, True)
    log_args = [file]
    add_log(30, "fn:XF_SERIALIZING.serializing() -file: {0[0]} dumped", log_args)

def load (file):
    """线性化对象载入"""
    try:
        with open(file, "rb") as f:
            _obj = pickle.load(f)
        log_args = [file]
        add_log(30, "fn:XF_SERIALIZING.load() -file: {0[0]} loaded", log_args)
        return _obj
    except FileNotFoundError:
        log_args = [file]
        add_log(20, "fn:XF_SERIALIZING.load() -except: FileNotFoundError {0[0]}", log_args)
        return
    except:
        log_args = [sys.exc_info()[0]]
        add_log(20, "fn:XF_SERIALIZING.load() -unknowexcept except: {0[0]}. File did not load", log_args)
        return
