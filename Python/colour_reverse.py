# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 02:34:31 2017

@author: Zero
"""

import cv2
import numpy as np

fn = "test1.jpg"

if __name__ == '__main__':
    print 'loading %s ...' % fn
    print 'processing'
    img=cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]
    
    b,g,r = cv2.split(img)
    b = 255-b
    g = 255-g
    r = 255-r
    img[:,:,0] = b
    img[:,:,1] = g
    img[:,:,2] = r
    
    mh = h/2
    mw = w/2

cv2.putText(img, "Hello world!", (mw,mh), cv2.FONT_HERSHEY_PLAIN, 2.0, (0,0,0), thickness = 2)

cv2.namedWindow('img')
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()