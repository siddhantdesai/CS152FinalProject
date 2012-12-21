# Erin and Vivian's Final Projec
# Facial Emotion Identifcation
# CS 152 - Neural Networks

# Image Parsing

#from getAllFiles import *
from constants import *

import os, sys
import re

import cv
import numpy as np
import scipy
import matplotlib.pyplot as plt



def getAllFiles(ext):
    """
    Retrieves the list of files in current directory
    Assumes that the top level folder is in current directory
    
    Input type: String(ext)
    Return type: String(currDir), [String(filenames)]
    """

    currDir = os.getcwd();
    currDir += ext;
    filenames = os.listdir(currDir);
    filenames.pop(0) # to get rid of the github hidden file
    return currDir, filenames;



def hot(fileList):
    """
    Parses the files and returns a list of only relevant images and their
    hot codes.

    Input type: fileList
    Return type: fileList
    """

    total = 0;
    finalFileList = [];
    nFiles = len(fileList);
    for i in range(nFiles):
        filename = fileList[i];
        
        # split filenames to get components
        arr = re.split(r"[_.]",filename);

        arrDir = arr[DIR];
        arrEmo = arr[EMOTION];
        arrOpen = arr[OPEN];
        
        success = False;
        # We only want to look at pictures that are straight on
        # and don't have glasses
        if 'straight' == arrDir and 'open' == arrOpen:
            # initialize hot code
            hotCode = [0,0,0,0];
            success = True;
            if 'angry' == arrEmo:
                hotCode[ANGRY] = 1;
            elif 'happy' == arrEmo:
                hotCode[HAPPY] = 1;
            elif 'neutral' == arrEmo:
                hotCode[NEUTRAL] = 1;
            elif 'sad' == arrEmo:
                hotCode[SAD] = 1;
            else:
                print 'No emotion data';
                success = False;
        
        if success:
            finalFileList.append([filename, hotCode]);
            total = total + 1;

    print "total: ", total;
    print "first file and code: ", finalFileList[0]

    return finalFileList


def read_pgm(filename, byteorder='>'):
    """Return image data from a raw PGM file as numpy array.

    Format specification: http://netpbm.sourceforge.net/doc/pgm.html

    """
    with open(filename, 'rb') as f:
        buffer = f.read()
    try:
        header, width, height, maxval = re.search(
            b"(^P5\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
    except AttributeError:
        raise ValueError("Not a raw PGM file: '%s'" % filename)
    return numpy.frombuffer(buffer,
                            dtype='u1' if int(maxval) < 256 else byteorder+'u2',
                            count=int(width)*int(height),
                            offset=len(header)
                            ).reshape((int(height), int(width)))


if __name__=="__main__":

    currDir, fileList = getAllFiles("/all_images");

    finalFileList = hot(fileList)

    num_samples = len(finalFileList)

    arr = []
    for sample in range(num_samples):
        path = currDir + '/' + finalFileList[sample][0];
        hotCode = finalFileList[sample][1]
        
        face = cv.LoadImageM(path, cv.CV_LOAD_IMAGE_GRAYSCALE);
        a = np.asarray( face[:,:] )
        nRow, nCol = a.shape
        curr = []
        for row in range(nRow):
            for val in a[row]:
                curr.append(val)s

        arr.append(curr)

##    print len(arr), len(arr[0])
##    print len(arr)*len(arr[0])
##    b = np.array(arr[0])
##    for row in range(1, len(arr)):
##        a = np.array(arr[row])
##        b = np.concatenate((b,a), axis=0)
##
##    b.reshape((num_samples, len(arr[0])))
##    print b.shape
##    np.savetxt('image_data.txt', b)


##    # experiement on the first image
##    a = np.array(arr[0])
##    size = a.size
##    np.savetxt('first_face.txt', a)
##
##    # make the image come back
##    new_data = np.loadtxt('first_face.txt')
##    new_data = new_data.reshape((120,128))
##
##    plt.imshow(new_data) #Needs to be in row,col order
##    plt.savefig('haha.png')
 

##    # Save data to a text file using numpy
##    x = np.arange(20).reshape((4,5))
##    np.savetxt('test.txt', x)
##
##    # To read info back using numpy
##    new_data = np.loadtxt('test.txt')
##    new_data = new_data.reshape((4,5))


    # display first image for testing
##    index = 0;
##    path = currDir + '/' + finalFileList[index][0];
##    face = cv.LoadImage(path, cv.CV_LOAD_IMAGE_GRAYSCALE);
##    windowTitle = "face: " + str(index);
##    cv.ShowImage(windowTitle, face);
