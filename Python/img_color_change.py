# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:13:58 2017

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
    ii=0
    for xi in xrange(0,w):
        for xj in xrange(0,h):
            img[xj,xi,0] = int(img[xj,xi,0]*0.2) #blue
            img[xj,xi,1] = int(img[xj,xi,1]*0.2) #green
            img[xj,xi,2] = int(img[xj,xi,2]*0.2) #red
        if xi&10==0 :print '.',
#        if xi%10==0 :print '.',
cv2.namedWindow('img')
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()

#        cv2.namedWindow('img')
#        cv2.imshow('img',img)
#        cv2.waitKey()
#        cv2.destroyAllWindows()