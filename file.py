import os
from os import path
import threading
import time
import polling2

dir = "F:\python"
date = "20200304"


all_files = ['amc_20200304.txt', 'hello.py', 'pmc_20190807.txt', 'pmc_20200304.txt', 'pmc_20304.txt']
req_text = ['pmc_20304', 'abc']

# checking for files to be available
def file_check():    
    all_files = os.listdir(dir)
    print('Checking for required files...')
    for r in req_text:
        found = False
        for f in all_files:    
            if r in f:                         
                found = True
                break
        if not found:
            return False
    return f, True
          
# polling to check if file exists or not
def poll_file_check():
    result = file_check()
    print(result)
    try:
        polling2.poll(file_check, timeout=20, step=5 )
        print("files are available")
    except Exception as tee:
        print("files are not available")

poll_file_check()
'''
# call poll_file_check function after 30 seconds
def print_poll():
    t = threading.Timer(30.0, poll_file_check)
    t.start()
  
  

print_poll()

'''


