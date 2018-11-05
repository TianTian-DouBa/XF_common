from datetime import datetime, timedelta
import pytz
import tzlocal
from XF_common.XF_LOG_MANAGE import add_log

local_timezone = tzlocal.get_localzone()

def utc_to_local(utc_time):
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    return local_time

def local_to_utc(local_time):
    utc_time = local_time.astimezone(pytz.utc)
    return utc_time

def time_adjust_m30M(raw_time):
    """adjust time -30 minutes"""
    if not isinstance(raw_time, datetime):
        log_args = [raw_time]
        add_log(10, 'fn:time_adjust_m30M -raw_time "{0[0]}" is not type of datetime', log_args)
        return
    _time_delta = timedelta(minutes=-30)
    result = raw_time + _time_delta
    log_args = [result]
    add_log(40, 'fn:time_adjust_m30M -return "{0[0]}"', log_args)
    return result

def frac_to_msec(dt_sec_time, frac_sec):
    """convert SOE Date_Time and FracSec to datetime
    -dt_sec_time: in <datetime>
    -frac_sec: in int 0~9999"""
    msec = frac_sec / 10000
    result = dt_sec_time + timedelta(seconds=msec)
    assert isinstance(result, datetime)
    log_args = [result]
    add_log(40, 'fn:frac_to_msec -return "{0[0]}"', log_args)
    return result

def string_to_dt(string):
    """convert string '2018-08-16 13:34:23' to datetime"""
    result = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    log_args = [result]
    add_log(40, 'fn:string_to_dt -return "{0[0]}"', log_args)
    return result

def sp_string_to_dt(string,rule):
    """convert a specific string to datetime 2018-08-16 13:34:23.2310
    -return:<datetime>
    -string:<string> raw string e.g. '10/16/2018 12:00:16 PM 500ms'
    -rule:<string> e.g."""
    result = datetime.strptime(string, rule)
    log_args = [result]
    add_log(40, 'fn:sp_string_to_dt -return "{0[0]}"', log_args)
    return result

def dtmsec_to_string(dtmsec):
    """convert datetime with million seconds to string format '2018-08-18 13:46:51' and frac_sec 0~9999.
    dtmesc: <datetime>
    return: ('2018-08-16 13:34:23',231)"""
    _microsec = dtmsec.microsecond
    _dt = dtmsec - timedelta(microseconds=_microsec)
    dt_str = _dt.strftime('%Y-%m-%d %H:%M:%S')
    frac_sec = int(_microsec / 100)
    result = (dt_str, frac_sec)
    log_args = [result]
    add_log(40, 'fn:dtmsec_to_string -return "{0[0]}"', log_args)
    return result

def dtmsec_to_dt_and_frac(dtmsec):
    """convert datetime with million seconds to datetime fine to second and frac_sec 0~9999.
    dtmesc: <datetime>
    return: (<datetime> like 2018-08-16 13:34:23,231)"""
    _microsec = dtmsec.microsecond
    dt = dtmsec - timedelta(microseconds=_microsec)
    frac_sec = int(_microsec / 100)
    result = (dt, frac_sec)
    log_args = [result]
    add_log(40, 'fn:dtmsec_to_dt_and_frac -return "{0[0]}"', log_args)
    return result

def dt_f_to_string(dt):
    """display datetime in the format of '2018-08-16 13:34:23.231'
    -dt: <datetime>"""
    result = dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:24]
    log_args = [result]
    add_log(40, 'fn:dt_f_to_string -return "{0[0]}"', log_args)
    return result

def dt_to_string(dt):
    """display datetime in the format of '2018-08-16 13:34:23'
    -dt: <datetime>"""
    result = dt.strftime("%Y-%m-%d %H:%M:%S")
    log_args = [result]
    add_log(40, 'fn:dt_to_string -return "{0[0]}"', log_args)
    return result
