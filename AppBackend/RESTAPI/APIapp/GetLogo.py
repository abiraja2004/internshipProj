import requests
import cv2
import urllib
import numpy as np
import cv2Testing
from skimage import io
import cStringIO
from PIL import Image

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

def main(company):
    # url = searchBingImage('mode.ai')['thumbnailUrl']
    # Url of image is inputted here and converted to image for cv2
    url = 'http://logo.clearbit.com/{}'.format(company)
    print url
    image = url_to_image(url)
    # print image
    # Starts the template matching
    for mmap in os.listdir('/Users/Hallshit/Documents/KnowledgeVC/AppBackend/RESTAPI/APIapp/marketMaps'):
        print mmap
        if cv2Testing.searchLogoInMap(image, '/Users/Hallshit/Documents/KnowledgeVC/AppBackend/RESTAPI/APIapp/marketMaps/{}'.format(mmap)) == True:
            return mmap

print main('mindsharemed.com')


# Optimize, Image Cropping, look for color, move out until n whitespace