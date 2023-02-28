from imageprocessing import *
from blockpicker import *
import numpy as np
maxheight = 320

pixelsperblock = resize_and_save_image(maxheight)

imagestoprocess = split_image('resizedimage.jpg', pixelsperblock)
print(str(len(imagestoprocess)) + ' images have just been processed.')

processedimages = get_closest_image(imagestoprocess)


feez = combine_images(processedimages, pixelsperblock)
feez.save('deez.jpg')


