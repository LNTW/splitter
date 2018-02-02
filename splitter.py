import os
import re

file_to_split = raw_input("What is the file name?")
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path,file_to_split)[:-3]

try:
    os.makedirs(directory)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

file_obj = open(file_to_split, 'r')
big_string = file_obj.read()
file_obj.close()
#file_list = re.split('M30', big_string)
file_list=re.split('(?<=M30).|(?<=M99).', big_string)
for nc_file in file_list :
    try :
        file_name = nc_file.split('(')[1].split(')')[0].strip()
    except :
        try: 
            file_name = nc_file.split('O')[1].split('\r')[0]                    
        except :
            print 'yikes!' , nc_file
            continue
    # Make the program name windows compliant, as some programs are sent to windows based cnc
    print file_name
    reg = re.compile(r'[< > : " / \\ | ? *]')
    file_name = reg.sub('_', file_name)
    if file_name[-3:] != '.NC' :
        file_name += '.NC'
    a = open(directory + '/' + file_name, "w")
    a.write(nc_file)
    a.close()

