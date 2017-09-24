#coding:utf-8

import urllib
def download(url):
    if url is None:
        return None
    response = urllib.urlopen(url)
        
    if response.getcode()!=200 :
        return None
    return response.read()
    

