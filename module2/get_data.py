
#print(__name__)
"""Download data from our server
"""

import requests
import shutil
import os
import urllib
from urllib.request import urlretrieve

server_url = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'

def download_file(url, file_name):
    # TODO: Download to pwd (present working directory)
    pass

def unzip_file(file_name):
    # TODO: Unzip file
    pass

def main():
    """Driven Function
    """
    data = 'pandas01Data.zip'
    #download_file(server_url, data)
    #unzip_file(data)
    print(urlretrieve(server_url, data))
    

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point