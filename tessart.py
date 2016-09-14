# -*- coding: utf-8 -*-
from PIL import Image
import os, time, sys
from PIL import Image

from PIL import ImageFilter
from PIL import ImageEnhance
names = locals()

im = Image.open('1.jpg')
im = ImageEnhance.Contrast(im).enhance(20).convert('L')
im = ImageEnhance.Sharpness(im).enhance(2)

im = im.crop((1175,500,1500,600))

im.save('new.png')
from pytesseract import image_to_string
print (image_to_string(im,  lang='chi_sim'))
print (image_to_string(im, lang='fra'))