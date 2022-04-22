import os
import shutil
from datetime import date
from pathlib import Path
####inputtrace
def file_move_input():
    #move
    srcf = '//gcait/c$/Program Files (x86)/NCR/BIS/Logs/InputTrace.log'
    destf = 'S:\\ITMs\\BISTracelogs\\InputTraceLogsOLD\\'
    shutil.move(srcf, destf)

def file_rename_input():
    grab_date = date.today()  # get date
    format_date = grab_date.strftime('%Y%m%d')  # format date into yyyymmdd
    old = os.path.join('S:\\ITMs\\BISTracelogs\\InputTraceLogsOLD\\', 'InputTrace.log')
    new = os.path.join('S:\\ITMs\\BISTracelogs\\InputTraceLogsOLD\\', 'InputTrace{date}.log'.format(date=format_date))
    os.rename(old,new)

####outputtrace
def file_move_output():
    #move
    srcf = '//gcait/c$/Program Files (x86)/NCR/BIS/Logs/OutputTrace.log'
    destf = 'S:\\ITMs\\BISTracelogs\\'
    shutil.move(srcf, destf)

def file_rename_output():
    grab_date = date.today()  # get date
    format_date = grab_date.strftime('%Y%m%d')  # format date into yyyymmdd
    old = os.path.join('S:\\ITMs\\BISTracelogs\\OutputTraceLogsOLD\\', 'OutputTrace.log')
    new = os.path.join('S:\\ITMs\\BISTracelogs\\OutputTraceLogsOLD\\', 'OutputTrace{date}.log'.format(date=format_date))
    os.rename(old,new)


file_move_input()
file_rename_input()
file_move_output()
file_rename_output()