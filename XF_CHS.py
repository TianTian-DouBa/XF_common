from XF_common.XF_LOG_MANAGE import *
from subprocess import Popen

CHS_PATH = r"C:\DeltaV\Bin\CHS.exe"

def run_chs(start_s,end_s,trends_s):
    """create and open the trends group
    - start_s:<string>start time string, local time zone, e.g. r'"2018-11-01 13:07:25"'
    - end_s:<string>end time string, local time zone, e.g. r'"2018-11-03 17:22:19"'
    - trends_s:<string> e.g. "(MODULE1/PARAMETER.CV, MODULE1/PARAMETER.CV, , , V1-COMMON/BATCH_ID.CV)"
    """
    #start_s = r'"2018-11-01 13:07:25"'
    #end_s = r'"2018-11-03 17:22:19"'
    #trend_s = r"(SIM-001/SIN.CV, SIM-001/RAMP.CV, , , V1-COMMON/BATCH_ID.CV)"
    Popen([CHS_PATH, [r'/new',' EChart', r' /starttime ', start_s, r' /endtime ', end_s, r' /trend ', trends_s]])

if __name__ == '__main__':
    run_chs()
