import requests
import cv2
import urllib
import numpy as np
import cv2Testing
from skimage import io
import cStringIO
from PIL import Image
from multiprocessing import Pool
from functools import partial

import os

url = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search?q=sailing+dinghies&mkt=en-us'
key = 'de3f72b2be214696a665ef1ef67bbfe4'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
}


def url_to_image(url):
    image = io.imread(url)
    return image

def searchBingImage(q):
    q = q + " logo"
    url = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search?'
    params = {'q': q}
    headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
    }

    r = requests.get(url, headers=headers, params=params)
    results = r.json()
    # print results
    try:
        results = results['queryExpansions'][0]
        return results['thumbnail']
    except:
        results = results['value'][0]
        return results

def log_result(arg):
    print arg






def main(company):
    # url = searchBingImage('mode.ai')['thumbnailUrl']
    # Url of image is inputted here and converted to image for cv2
    url = 'http://logo.clearbit.com/{}'.format(company)
    print url
    image = url_to_image(url)

    #

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    origmmaps = []
    mmaps = []
    for mmap in os.listdir('/Users/Hallshit/Documents/KnowledgeVC/AppBackend/RESTAPI/APIapp/marketMaps'):
        origmmaps.append(mmap)
        mmaps.append(cv2.imread('/Users/Hallshit/Documents/KnowledgeVC/AppBackend/RESTAPI/APIapp/marketMaps/{}'.format(mmap), 0))
    # print mmaps
    p = Pool()
    func = partial(cv2Testing.searchLogoInMap, image)
    result = p.map(func, mmaps)
    # for m in mmaps:
    #     # print m
    #     result = p.apply_async(func, args=m, callback=log_result)
    p.close()
    p.join()
    print result


    for i, x in enumerate(result):
        if x == True:
            return origmmaps[i]

        # print mmap
        # if cv2Testing.searchLogoInMap(image, '/Users/Hallshit/Documents/KnowledgeVC/AppBackend/RESTAPI/APIapp/marketMaps/{}'.format(mmap)) == True:
        #     return mmap

# print main('bons.ai')


# Optimize, Image Cropping, look for color, move out until n whitespace