import hashlib
import time
import os
from operator import itemgetter

from PIL import Image

from .vectorspace import *


class TxtCracker:
    def __init__(self):
        self.data = "./data"
        self.model = "./model"
        return None

    def buildVector(self, im):
        d1 = {}
        count = 0
        for i in im.getdata():
            d1[count] = i
            count += 1
        return d1

    def runme(self):
        v = VectorCompare()
        
        iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        imageset = []

        for letter in iconset:
            for img in os.listdir(f"{self.model}/iconset/{letter}"):
                temp = []
                temp.append(self.buildVector(Image.open(f"{self.model}/iconset/{letter}/{img}")))
                imageset.append({letter:temp})

        im = Image.open(f"{self.data}/captcha.gif")
        im2 = Image.new("P",im.size,255)
        im = im.convert("P")

        hist = im.histogram()
        values = {}
        for i in range(256):
            values[i] = hist[i]
        colours = sorted(values.items(), key=itemgetter(1), reverse=True)[:10]
        print(colours)
        txt1 = colours[1][0] if colours[1][0] != 0 else colours[2][0]
        txt2 = txt1
        diff = 999999
        for colour,qty in colours:
            df = abs(txt1 - colour)
            if df < diff and df > 0:
                diff = df
                txt2 = colour
        temp = {}
        print(txt1,txt2)
        exit(0)
        for x in range(im.size[1]):
            for y in range(im.size[0]):
                pix = im.getpixel((y,x))
                temp[pix] = pix
                if pix == txt1 or pix == txt2: # these are the numbers to get
                    im2.putpixel((y,x),0)

        inletter = False
        foundletter=False
        start = 0
        end = 0

        letters = []
        
        for y in range(im2.size[0]): # slice across
            for x in range(im2.size[1]): # slice down
                pix = im2.getpixel((y,x))
                if pix != 255:
                    inletter = True

            if foundletter == False and inletter == True:
                foundletter = True
                start = y

            if foundletter == True and inletter == False:
                foundletter = False
                end = y
                letters.append((start,end))

            inletter=False

        count = 0
        for letter in letters:
            m = hashlib.md5()
            im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
            
            guess = []
            
            for image in imageset:
                for x,y in image.items():
                    if len(y) != 0:
                        guess.append((v.relation(y[0],self.buildVector(im3)),x))
            
            guess.sort(reverse=True)
            print(f"{guess[0]}")

            count += 1

if __name__ == '__main__':
    txt_cracker = TxtCracker()
    txt_cracker.runme()
