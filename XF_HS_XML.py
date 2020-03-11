import xml.etree.cElementTree as et
from lxml import etree
from subprocess import run
from io import StringIO
from XF_common.XF_LOG_MANAGE import *
from XF_common.XF_UTC_LOCAL import dt_to_string, sp_string_to_dt
from XF_common.XF_DV_HIST import Value_Log
from datetime import datetime, timedelta

XML_CONSTANT = {'raw_1pt':{'xml_path':r'.\packed\temp\_raw_1pt.tmp','result_path':r".\packed\temp\raw_1pt_opt.xml"},\
'raw_mpt':{'xml_path':r'.\packed\temp\_raw_mpt.tmp','result_path':r'.\packed\temp\raw_mpt_opt.xml'}}
def load_xml(path):
    """加载xml文件，返回et.ElementTree对象
    -path: 存放XML文件的路径"""
    try:
        tree = et.ElementTree(file=path)
        return tree
    except FileNotFoundError:
        log_args = [path]
        add_log(30, 'file not found. --"{0[0]}"', log_args)

def create_raw_1pt_xml(dt,item_id,host = 'localhost'):
    """create the xml for 1 raw sample before time
    -return:<et.ElementTree>
    -dt:<datetime> UTC time or <None>
    -host:<string> e.g. 'localhost'
    -item_id:<string> e.g. 'V1-COMMON/BATCH_ID.CV'"""
    xml_string = r'''
    <DeltaVOpcHdaClient>
      <Configuration>
        <OutputFileName>raw_1pt_opt</OutputFileName>
        <OutputDirectory>.\packed\temp</OutputDirectory>
        <OutputFileFormat>XML</OutputFileFormat>
        <LogFileName>log_raw_1pt</LogFileName>
        <LogFileDirectory>.\packed\temp</LogFileDirectory>
        <TimeSetting>UTC</TimeSetting>
        <HostName>localhost</HostName>
      </Configuration>
      <Execution>
        <Steps>
          <Step>
            <Interface>IOPCHDA_SyncRead</Interface>
            <Method>ReadRaw</Method>
            <ItemID>MODULE/PARAMETER.CV</ItemID>
            <StartTime>2018-10-01 02:15:17</StartTime>
            <EndTime>2018-10-01 02:15:17</EndTime>
            <NumValues>1</NumValues>
            <Bounds>TRUE</Bounds>
          </Step>
        </Steps>
      </Execution>
    </DeltaVOpcHdaClient>
    '''
    root = et.fromstring(xml_string)
    _host_name = root.find("./Configuration/HostName")
    _host_name.text = host
    _item_id = root.find("./Execution/Steps/Step/ItemID")
    _item_id.text = item_id
    if isinstance(dt,datetime):
        dt_str = dt_to_string(dt)
    else:
        dt_str = dt_to_string(datetime.utcnow())
    _start_time = root.find("./Execution/Steps/Step/StartTime")
    _end_time = root.find("./Execution/Steps/Step/EndTime")
    _start_time.text = dt_str
    _end_time.text = dt_str
    element_tree = et.ElementTree(root)
    return element_tree

def create_raw_mpt_xml(start_time,end_time,item_id,host = 'localhost'):
    """create the xml for 1 raw sample before time
    -return:<et.ElementTree>
    -start_time:<datetime> UTC time
    -end_time:<datetime> UTC time or <None>
    -host:<string> e.g. 'localhost'
    -item_id:<string> e.g. 'V1-COMMON/BATCH_ID.CV'"""
    xml_string = r'''
    <DeltaVOpcHdaClient>
      <Configuration>
        <OutputFileName>raw_mpt_opt</OutputFileName>
        <OutputDirectory>.\packed\temp</OutputDirectory>
        <OutputFileFormat>XML</OutputFileFormat>
        <LogFileName>log_raw_mpt</LogFileName>
        <LogFileDirectory>.\packed\temp</LogFileDirectory>
        <TimeSetting>UTC</TimeSetting>
        <HostName>localhost</HostName>
      </Configuration>
      <Execution>
        <Steps>
          <Step>
            <Interface>IOPCHDA_SyncRead</Interface>
            <Method>ReadRaw</Method>
            <ItemID>MODULE/PARAMETER.CV</ItemID>
            <StartTime>2018-10-01 02:15:17</StartTime>
            <EndTime>2018-10-01 02:15:17</EndTime>
            <NumValues>0</NumValues>
            <Bounds>TRUE</Bounds>
          </Step>
        </Steps>
      </Execution>
    </DeltaVOpcHdaClient>
    '''
    root = et.fromstring(xml_string)
    _host_name = root.find("./Configuration/HostName")
    _host_name.text = host
    _item_id = root.find("./Execution/Steps/Step/ItemID")
    _item_id.text = item_id
    start_time_str = dt_to_string(start_time)
    _start_time = root.find("./Execution/Steps/Step/StartTime")
    _start_time.text = start_time_str
    if isinstance(end_time,datetime):
        end_time_str = dt_to_string(end_time)
    else:
        end_time_str = dt_to_string(datetime.utcnow())
    _end_time = root.find("./Execution/Steps/Step/EndTime")
    _end_time.text = end_time_str
    element_tree = et.ElementTree(root)
    return element_tree

def create_itv_1pt_xml(dt,item_id,host = 'localhost',interval = 14400):
    """to be modified
    create the xml for 1 interval sample before time
    -return:<et.ElementTree>
    -dt:<datetime> UTC time
    -item_id:<string> e.g. 'V1-COMMON/BATCH_ID.CV'
    -host:<string> e.g. 'localhost'
    -interval:<int> in seconds
    """
    xml_string = r'''
    <DeltaVOpcHdaClient>
      <Configuration>
        <OutputFileName>itv_1pt_opt</OutputFileName>
        <OutputDirectory>.\packed\temp</OutputDirectory>
        <OutputFileFormat>XML</OutputFileFormat>
        <LogFileName>log_itv_1pt</LogFileName>
        <LogFileDirectory>.\packed\temp</LogFileDirectory>
        <TimeSetting>UTC</TimeSetting>
        <HostName>localhost</HostName>
      </Configuration>
      <Execution>
        <Steps>
          <Step>
            <Interface>IOPCHDA_SyncRead</Interface>
            <Method>ReadProcessed</Method>
            <ItemID>MODULE/PARAMETER.CV</ItemID>
            <StartTime>2018-10-01 02:15:17</StartTime>
            <EndTime>2018-10-01 02:15:17</EndTime>
            <ResampleInterval>600000</ResampleInterval>
            <NumValues>1</NumValues>
            <Bounds>TRUE</Bounds>
          </Step>
        </Steps>
      </Execution>
    </DeltaVOpcHdaClient>
    '''
    root = et.fromstring(xml_string)
    _host_name = root.find("./Configuration/HostName")
    _host_name.text = host
    _item_id = root.find("./Execution/Steps/Step/ItemID")
    _item_id.text = item_id
    dt_str = dt_to_string(dt)
    _start_time = root.find("./Execution/Steps/Step/StartTime")
    _end_time = root.find("./Execution/Steps/Step/EndTime")
    _start_time.text = dt_str
    _end_time.text = dt_str
    _interval = root.find("./Execution/Steps/Step/ResampleInterval")
    _interval.text = str(interval*1000)
    element_tree = et.ElementTree(root)
    return element_tree

def read_mpt(xml_path):
    """read the lis of (value, time_stamp, quality).
    -return:<[(value,time_stamp<dt UTC>,quality<int>),...]>
    -xml_path:<string> e.g. r".\packed\temp\raw_1pt_opt.xml"""
    result = []
    tree = load_xml(xml_path)
    root = tree.getroot()
    _data_value = root.findall("./Item/DataValue")
    for log in _data_value:
        value_log = Value_Log()
        value_log.value = log.text
        _time_string = log.attrib['TimeStamp']
        value_log.time_stamp = _str_to_time(_time_string)
        _quality = log.attrib['Quality']
        value_log.quality = int(_quality)
        result.append(value_log)
    if logable(30):
        item = root.find("./Item")
        item_id = item.attrib['ItemID']
        log_print('[fn]read_mpt().ItemID:{} start----'.format(item_id))
        for _rslt in result:
            log_args = [_rslt.value,_rslt.time_stamp,_rslt.quality]
            add_log(30, '    .value:"{0[0]}", .time_stamp:"{0[1]}", .quality:"{0[2]}"', log_args)
        log_print('[fn]read_mpt().ItemID:{} end----'.format(item_id))

    return result

def read_1pt(xml_path):
    """read the value, time_stamp and quality.
    -return:<XF_DV_HIST.Value_Log> or None
    -xml_path:<string> e.g. r".\packed\temp\raw_1pt_opt.xml"""
    tree = load_xml(xml_path)
    root = tree.getroot()
    _data_value = root.find("./Item/DataValue")
    if _data_value == None:
        add_log(40, 'fn:read_1pt.reuslt=None, no new data')
        return None
    value = _data_value.text
    _time_string = _data_value.attrib['TimeStamp']
    time_stamp = _str_to_time(_time_string)
    log_args = [time_stamp]
    add_log(40, '[fn]read_raw_1pt().time_stamp --"{0[0]}"', log_args)
    _quality = _data_value.attrib['Quality']
    quality = int(_quality)
    result = Value_Log()
    result.value = value
    result.time_stamp = time_stamp
    result.quality = quality
    if logable(30):
        item = root.find("./Item")
        item_id = item.attrib['ItemID']
        log_print('[fn]read_raw_1pt().ItemID:{}'.format(item_id))
    log_args = [result.value,result.time_stamp,result.quality]
    add_log(30, '[fn]read_raw_1pt().value:"{0[0]}", .time_stamp:"{0[1]}", .quality:"{0[2]}"', log_args)
    return result

def _str_to_time(time_string):
    """guide two differnet HDA returned time string format to the right rule and return <datetime>"""
    rule1 = "%m/%d/%Y %I:%M:%S %p %fms"
    rule2 = "%m/%d/%Y %I:%M:%S %p"
    log_args = [time_string]
    add_log(40, '[fn]_str_to_time().time_string --"{0[0]}"', log_args)
    try:
        result = sp_string_to_dt(time_string, rule1)
    except ValueError:
        result = sp_string_to_dt(time_string, rule2)
    log_args = [result]
    add_log(40, '[fn]_str_to_time().result --"{0[0]}"', log_args)
    return result

def generate_xml(element_tree,path):
    """generate the xml file from et.root
    -element_tree:<et.ElementTree>
    -path:<string> e.g. r".\packed\_raw_1pt.tmp"""
    with open(path, 'w') as f:
        element_tree.write(f, encoding='unicode', short_empty_elements=False)

def valid_xml(xsd_path,xml):
    """validate .xml file with .xsd file
    -xsd_path: <string> path of file. e.g. r'.\XF_XML_sub\DvOpcHda.xsd'
    -xml: <steam> read from file or StringIO
    """
    with open(xsd_path,'r') as xsd:
        xmlschema_doc = etree.parse(xsd)
        xmlschema = etree.XMLSchema(xmlschema_doc) #construct a XMLSchema validator
        xml_to_valid = etree.parse(xml)
    try:
        xmlschema.assertValid(xml_to_valid)
        add_log(30,'[fn] XF_XML.valid_xml: Pass')
    except etree.DocumentInvalid as e:
        log_args = [e]
        add_log(10,'[fn] XF_XML.valid_xml: "{0[0]}"',log_args)

if __name__ == '__main__':
    with open(r'.\XF_XML_sub\OpcHdaTST001.xml','r') as xml:
        valid_xml(r'.\XF_XML_sub\DvOpcHda.xsd',xml)
