# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:37:39 2017

@author: Zero
"""

import cv2
import numpy as np

fn = "test1.jpg"
if __name__ == '__main__':
    print 'loading %s ...' % fn
    print u'processing',
    img=cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]
    ii=0
    
    mirror_w = w/2
    
#print "w is: ", w
#print "mirror_w is: ", mirror_w
    
    for xj in xrange(0,h):
        for xi in xrange(0,mirror_w):
#            img[xj,xi,:] = img[xj,w - xi - 1,:]
            img[xj,xi,:] = img[xj,w - xi - 1,:]
            
            print '.',
            
cv2.namedWindow('img')
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()