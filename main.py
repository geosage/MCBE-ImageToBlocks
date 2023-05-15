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
    # Get the filename of the selected image
    selected_filename = os.path.basename(file_path)
    
    # Get the base name of the selected image (without the extension)
    selected_basename = os.path.splitext(selected_filename)[0]
    
    # Open the image
    with Image.open(file_path) as img:
        # Save the image as mainimage.png
        img.save(f"mainimage.png")
        print(f"Successfully uploaded image '{selected_basename}'")
else:
    print("No file selected")
#------------------------------------------

print(selected_basename)

maxheight = 320 #Max block height
q = 1
importquestion = True
pixelsperblock = resize_and_save_image(maxheight)

#Split Image - imageprocessing.py
imagestoprocess, columns = split_image('resizedimage.jpg', pixelsperblock)
print(str(len(imagestoprocess) * len(imagestoprocess[0])) + ' images are being processed.')

imagesnum = len(imagestoprocess) * len(imagestoprocess[0])

#Get Closest Images - blockpicker.py
processedimages, imagenames = get_closest_image(imagestoprocess)

#Combine and Save Images - imageprocessing.py
feez, num_rows, num_cols = combine_images(processedimages)
feez.save('finalimage.jpg')

print(str(columns) + ' Columns')

#Open Image
os.startfile('finalimage.jpg')

#Import Image - importmcbe.py
wantimport = str(input("Your final image has been opened. Do you want to import it? (Yes/No)")).lower()
while importquestion == True:
    if wantimport == "yes":
        joe = mcbequestion(imagenames, num_cols, selected_basename)
        importquestion = False
    elif wantimport == "no":
        quit()
    else:
        wantimport = str(input("Please pick Yes or No.")).lower()