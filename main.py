from imageprocessing import *
from blockpicker import *
from importmcbe import *

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
importquestion = True
pixelsperblock = resize_and_save_image(maxheight)

#Split Image
imagestoprocess, columns = split_image('resizedimage.jpg', pixelsperblock)
print(str(len(imagestoprocess) * len(imagestoprocess[0])) + ' images are being processed.')

imagesnum = len(imagestoprocess) * len(imagestoprocess[0])
#Get Closest Images
processedimages, imagenames = get_closest_image(imagestoprocess)

#Combine and Save Images
feez, num_rows, num_cols = combine_images(processedimages)
feez.save('finalimage.jpg')
print(imagenames)
print(str(columns) + ' Columns')

#Open Image
os.startfile('finalimage.jpg')

#Import Image
wantimport = str(input("Your final image has been opened. Do you want to import it? (Yes/No)")).lower()
while importquestion == True:
    if wantimport == "yes":
        joe = mcbeimage(imagenames, num_cols, num_rows)
        importquestion = False
    elif wantimport == "no":
        quit()
    else:
        wantimport = str(input("Please pick Yes or No.")).lower()