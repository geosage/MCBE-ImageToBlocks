from imageprocessing import *
from blockpicker import *
import numpy as np

import tkinter as tk
from tkinter import filedialog
from PIL import Image

#Image Upload ------------------------------
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.gif;*.bmp")])

if file_path:
    with Image.open(file_path) as img:
            img.save(f"mainimage.png")
            print("Successfully uploaded image")
else:
    print("No file selected")
#------------------------------------------

maxheight = 320
q = 1
pixelsperblock = resize_and_save_image(maxheight)

imagestoprocess, columns = split_image('resizedimage.jpg', pixelsperblock)
print(str(len(imagestoprocess) * len(imagestoprocess[0])) + ' images are being processed.')

processedimages, imagenames = get_closest_image(imagestoprocess)

feez = combine_images(processedimages)
feez.save('finalimage.jpg')
print(imagenames)
print(str(columns) + ' Columns')

os.startfile('finalimage.jpg')


#lol
