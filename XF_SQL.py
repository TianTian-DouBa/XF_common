import pymssql
from datetime import datetime
from XF_common.XF_LOG_MANAGE import *
from XF_common.XF_UTC_LOCAL import dtmsec_to_string

class DV_SOE():
    def __init__(self, server = 'localhost', db = 'EJournal'):
        """this 'localhost' is only able to work on station with SOE enabled"""
        try: #if SQL db is invalid
            self.conn = pymssql.connect(host=server + r'\DELTAV_CHRONICLE',
                           database=db)
            self.cursor = self.conn.cursor()
            self.sql = ''
        except: # pymssql.OperationalError:
            self.conn = None
            log_args = [server + r'\DELTAV_CHRONICLE', db]
            add_log(30,'fn:XF_SQL.DV_SOE.__init__();pymssql.connect faile; host={0[0]}, db={0[1]}',log_args)

    def enquiry(self, sql):
        """sql enquiry"""
        self.sql = sql
        self.cursor.execute(self.sql)
        result = self.cursor.fetchall()
        log_args = [sql]
        add_log(40, "fn:enquiry() -sql: {0[0]}", log_args)
        add_log(40, "fn:enquiry() -return start---------------------")
        if logable(40):
            for i in result:
                log_print(i)
        add_log(40, "fn:enquiry() -return end---------------------")
        return result

    def sql_batch_start(self, module, time_start, time_end = None):
        """generate the sql to enquiry BATCH_START parameter time in UTC.
        -return: sql in <str>; None if error
        -module: module name e.g. 'V1-COMMON'
        -time_start: <datetime.datetime> in UTC e.g. '2018-08-18 02:46:51.32130000'
        -time_end: <datetime.datetime> in UTC e.g. '2018-08-20 02:46:51.32130000'; or None"""
        #未来考虑验证module的有效性
        if not isinstance(time_start, datetime):
            log_args = [time_start]
            add_log(20, "fn:sql_batch_start() -time_start 'cv: {0[0]}' is not instance of datetime.", log_args)
            return
        if (not isinstance(module, str)) or module =='':
            add_log(20, "fn:sql_batch_start() -module is not valid.")
            return
        if not (isinstance(time_end, datetime) or time_end == None):
            add_log(20, "fn:sql_batch_start() -time_end is not valid.")
            return

        _t_start = dtmsec_to_string(time_start)
        if time_end != None:
            _t_end = dtmsec_to_string(time_end)
            sql = (r"select Replace (Journal.Desc2, 'NEW VALUE = ', '') ,"
            r" Journal.Date_Time, Journal.FracSec From Journal "
            r" Where (Journal.Date_Time > '" + _t_start[0] + r"'"
            r" Or (Journal.Date_Time = '" + _t_start[0] + r"'"
            r" And Journal.FracSec > " + str(_t_start[1]) + r"))"
            r" And (Journal.Date_Time < '" + _t_end[0] + r"'"
            r" Or (Journal.Date_Time = '" + _t_end[0] + r"'"
            r" And Journal.FracSec <= " + str(_t_end[1]) + r"))"
            r" And Journal.Desc2 Not Like '%None%'"
            r" And Journal.Desc2 Not Like ''"
            r" And Journal.Module Like '%" + module + "%'"
            r" And Journal.Attribute Like '%BATCH_START%'")
        else: #time_end is not specified
            sql = (r"select Replace (Journal.Desc2, 'NEW VALUE = ', '') ,"
            r" Journal.Date_Time, Journal.FracSec From Journal "
            r" Where (Journal.Date_Time > '" + _t_start[0] + r"'"
            r" Or (Journal.Date_Time = '" + _t_start[0] + r"'"
            r" And Journal.FracSec > " + str(_t_start[1]) + r"))"
            r" And Journal.Desc2 Not Like '%None%'"
            r" And Journal.Desc2 Not Like ''"
            r" And Journal.Module Like '%" + module + "%'"
            r" And Journal.Attribute Like '%BATCH_START%'")
        return sql

    def db_names(self):
        """reteive all the accessable db names"""
        sql = r"Select name from Sys.Databases"
        _rslt = self.enquiry(sql)
        result = []
        for s in _rslt:
            result.append(s[0])
        if logable(40):
            log_print("fn:db_name return start-----------------------")
            for i in result:
                log_print(i)
            log_print("fn:db_name return end-----------------------")
        return result

    def close(self):
        """close connection"""
        self.conn.close()

if __name__ == "__main__":
    print("===================XF_SQ.__main__ start===================")

    dv_soe = DV_SOE()
    sql = (r"select Replace(Journal.Desc2, 'NEW VALUE = ', '')"
       r" as Desc2, Journal.Date_Time, Journal.FracSec From Journal"
       r" Where Journal.Date_Time > '10-JULY-2016' And"
       r" Journal.Desc2 Not Like '%None%' And"
       r" Journal.Desc2 Not Like '' And"
       r" Journal.Module Like '%V1-COMMON%' And"
       r" Journal.Attribute Like '%BATCH_START%'")
    result = dv_soe.enquiry(sql)
    dv_soe.close()
    dv_soe = None

    for i in result:
        print(i)

    print("===========sql_batch_start();time_end=None (Start)============")
    dv_soe = DV_SOE()
    dt = datetime.strptime ("2018-08-18 02:47:25.8160", "%Y-%m-%d %H:%M:%S.%f")
    sql = dv_soe.sql_batch_start('V1-COMMON', dt)
    if sql:
        result = dv_soe.enquiry(sql)
        dv_soe.close()
        for i in result:
            print(i)
    dv_soe = None
    print("===========sql_batch_start();time_end=None (End)============")

    print("===========sql_batch_start(); (Start)============")
    dv_soe = DV_SOE()
    dt_start = datetime.strptime ("2018-08-18 02:47:25.8160", "%Y-%m-%d %H:%M:%S.%f")
    dt_end = datetime.strptime ("2018-09-13 15:21:10.0050", "%Y-%m-%d %H:%M:%S.%f")
    sql = dv_soe.sql_batch_start('V1-COMMON', dt_start, dt_end)
    if sql:
        result = dv_soe.enquiry(sql)
        dv_soe.close()
        for i in result:
            print(i)
    dv_soe = None
    print("===========sql_batch_start(); (End)============")

    print("=======================")
    dv_soe = DV_SOE()
    sql = r"Select name from Sys.Databases"
    result = dv_soe.enquiry(sql)
    dv_soe.close()
    dv_soe = None

    for i in result:
        print(i)

##dt_utc = rs[0][1]
##dt_local = utc_to_local(dt_utc)
##
##dt_utc = local_to_utc(dt_local)
##
##print(rs)
##print(dt_local)
##print(dt_local.strftime("%Y-%m-%d %H:%M:%S"))
##print(dt_utc)
##print(dt_utc.strftime("%Y-%m-%d %H:%M:%S"))
