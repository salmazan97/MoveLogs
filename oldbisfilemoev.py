import os
import shutil

def file_move_bis():
    dirpath = '//gcait/c$/Program Files (x86)/NCR/BIS/Logs/'
    dirlist = os.listdir(dirpath)

    for filename in dirlist:
        if 'BisTrace.txt2' in filename:
            srcf = '//gcait/c$/Program Files (x86)/NCR/BIS/Logs/' + filename
            destf = 'S:\\ITMs\\BISTracelogs\\BISTraceLogsOLD\\'
            shutil.move(srcf, destf)
            print('move complete')
        else:
            print('process complete')

file_move_bis()