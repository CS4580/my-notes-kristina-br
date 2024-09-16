
#print(__name__)
"""Download data from our server
"""

import requests
import shutil
import os, sys
import urllib
import zipfile

from urllib.request import urlretrieve

server_url = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'

def download_file(url, file_name):
    # TODO: Download to pwd (present working directory)
    pass

def extract_file(zip_path):
    # TODO: extract file to cwd/pwd
    #pass
    print(f'Extracting {zip_path}')
    # get the current wd
    extract_path = os.getcwd()

    # open file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # extract all the contents to the cwd
        zip_ref.extractall(extract_path)
        print(f'File unzipped successfull and extracted to {extract_path}')
        # list extracted files
        print(f'Extracted files: {zip_ref.namelist()}')



def main():
    """Driven Function
    """

    data = 'pandas01Data.zip'
    #download_file(server_url, data)
    #unzip_file(data)
    print(urlretrieve(server_url, data))
    

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point