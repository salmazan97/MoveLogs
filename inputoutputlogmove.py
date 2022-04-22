import os
import shutil
from datetime import date
from pathlib import Path
####
def file_move_input():
    #move
    srcf = 'filesource'
    destf = 'filedestination'
    shutil.move(srcf, destf)

def file_rename_input():
    grab_date = date.today()  # get date
    format_date = grab_date.strftime('%Y%m%d')  # format date into yyyymmdd
    old = os.path.join('filedestination', 'filename')
    new = os.path.join('filedestination', 'filename{date}'.format(date=format_date))
    os.rename(old,new)

####
def file_move_output():
    #move
    srcf = 'filesource'
    destf = 'filedestination'
    shutil.move(srcf, destf)

def file_rename_output():
    grab_date = date.today()  # get date
    format_date = grab_date.strftime('%Y%m%d')  # format date into yyyymmdd
    old = os.path.join('filedestination', 'filename')
    new = os.path.join('filedestination', 'filename{date}'.format(date=format_date))
    os.rename(old,new)


file_move_input()
file_rename_input()
file_move_output()
file_rename_output()
