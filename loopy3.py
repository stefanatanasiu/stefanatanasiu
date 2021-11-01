import os
import sys
import hashlib
import time
import sqlite3
import zlib
import datetime
from sqlite3 import Error

BLOCKSIZE = 524288

start_time = time.time()

#walk_dir = sys.argv[1]
walk_dir = "C:"
conn = sqlite3.connect('C:\DataSets\listing6.db')
c = conn.cursor()
# Create table
try:
    c.execute('''CREATE TABLE listing (file text, size number, hash text, last_modified real, listing_date real)''')
except Error as e:
    print(e)

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    #print('--\nroot = ' + root)
    #list_file_path = os.path.join(root, 'my-directory-list.txt')
    #print('list_file_path = ' + list_file_path)
    #for subdir in subdirs: 
        #print('--\nsubdir = ' + subdir )
    for file in files:
        #print('--\nfile = ' + file )
        file_path = os.path.join(root, file)
        #hasher=hashlib.blake2s()
        try: 
            f_asum = 1
            #with open(file_path, 'rb') as f:
            #    f_content = f.read(BLOCKSIZE)
            #    while len(f_content) > 0:
                    #hasher.update(f_content)
            #        f_asum = zlib.adler32(f_content, f_asum)
            #        f_content = f.read(BLOCKSIZE)
                #f_hash=hasher.hexdigest()
            #print('HASH: ' + str(f_asum)) 
            f_size=os.path.getsize(file_path)
            last_modified = os.path.getmtime(file_path)
            #print('Size: ' + str(f_size))
            #print('Last_modified: ' + str(last_modified))
            chestia = file_path, f_size, f_asum, last_modified, str(time.time())
            c.execute("INSERT INTO LISTING VALUES (?,?,?,?,?)",chestia)
            conn.commit()
        except Exception as e:
            print('Error: ' + file_path)
conn.close()
print("--- %s seconds ---" % (time.time() - start_time))


        