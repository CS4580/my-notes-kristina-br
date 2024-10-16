
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

        df = pd.read_csv(csv_file_name)
        return df


def extract_zip_file(zip_path):
    """Extracta ZIP file to the current working directory"""

    print(f"Extracting {zip_path}")
    # Get the current working directory
    extract_path = os.getcwd()

    # open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents to the current working directory
        zip_ref.extractall(extract_path)
        print(f"File unzipped successfully and extracted")
        # list the extracted files
        print(f"Extracted files: {zip_ref.namelist()}")

#TODO create a function to download the files
# from kaggle directly by passing the dataset name

def download_zip_file(url):
    pass

def main():
    """Driven Function
    """

    data = 'pandas01Data.zip'
    #download_file(server_url, data)
    #unzip_file(data)
    #print(urlretrieve(server_url, data))
    
    # if no arguments are provided, print a usage message
    #if len(sys.argv) < 2:
    #    print("something")

    url = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'
    #filename = 'pandas01Data.zip'
    query_parameters = 
    response = requests.get(url)
    #with open("gdp_by_country.zip")

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point