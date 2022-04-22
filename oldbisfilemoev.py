import os
import shutil

def file_move_bis():
    dirpath = 'directorypath'
    dirlist = os.listdir(dirpath)

    for filename in dirlist:
        if 'string' in filename:
            srcf = 'source' + filename
            destf = 'destination'
            shutil.move(srcf, destf)
            print('move complete')
        else:
            print('process complete')

file_move_bis()
