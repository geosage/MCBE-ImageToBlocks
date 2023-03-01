from imageprocessing import *
from blockpicker import *
import numpy as np
maxheight = 320
q = 1
pixelsperblock = resize_and_save_image(maxheight)

imagestoprocess = split_image('resizedimage.jpg', pixelsperblock)
print(str(len(imagestoprocess)) + ' images are being processed.')

#processedimages = get_closest_image(imagestoprocess)


feez = combine_images(imagestoprocess, pixelsperblock)
feez.save('deez.jpg')


