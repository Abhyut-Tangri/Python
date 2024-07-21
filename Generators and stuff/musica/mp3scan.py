import os 
import fnmatch
import di3reader as id3reader


def find_music(start,extension):
    for path, directories,files in os.walk(start):
        for file in fnmatch.filter(files,'+.{}'.format(extension)):
            yield os.path.join(path,file)

my_music_files=find_music('music','emp3')

error_list=[]
for f in my_music_files:
    try:
        id3r=id3reader.Reader(f)
        print('artists:{},album:{},track:{},song:'.format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')))
    except:
        error_list.append(f)
    
    
for error_file in error_list:
    print(error_file)