from PIL import Image
import math
import numpy as np

def resize_and_save_image(height_limit):
    filepath = "mainimage.png"
    def imagesize():
        img = Image.open(filepath)
        width = img.width
        height = img.height
        return height, width

    height, width = imagesize()

    while True:
        pixelsperblock_str = input("How many pixels do you want per block? ")
        try:
            pixelsperblock = int(pixelsperblock_str)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if height // pixelsperblock > height_limit:
            print("Please pick a larger number or your image will go above the height limit.")
        else:
            break

    def resize_image(image_path, target_size):
        img = Image.open(image_path)
        width, height = img.size

        target_width, target_height = target_size

        if width % target_width != 0 or height % target_height != 0:
            new_width = (width // target_width) * target_width
            new_height = (height // target_height) * target_height
            resized_img = img.resize((new_width, new_height))
        else:
            print(width, " and ", height, " are already divisible by ", pixelsperblock)
            resized_img = img

        return resized_img

    resized_img = resize_image(filepath, (pixelsperblock, pixelsperblock))

    if resized_img.mode == 'RGBA':
        bg = Image.new('RGBA', resized_img.size, (255, 255, 255, 255))
        bg.paste(resized_img, mask=resized_img.split()[3] if len(resized_img.split()) >= 4 else None)
        bg = bg.convert('RGB')
        bg.save('resizedimage.jpg')
    else:
        resized_img = resized_img.convert('RGB')
        resized_img.save('resizedimage.jpg')

    print("Original image dimensions:", height, "x", width)
    print("Resized image dimensions:", resized_img.height, "x", resized_img.width)
    print("Pixels per block:", pixelsperblock)
    return pixelsperblock



#-------------------------------------------------------------------------------------------
#Image Split And Combine
#-------------------------------------------------------------------------------------------

def split_image(image_path, size):
    # Open image and convert to numpy array
    img = Image.open(image_path)
    img_array = np.array(img)

    # Calculate number of rows and columns needed to split image into size*size sub-images
    rows = img_array.shape[0] // size
    cols = img_array.shape[1] // size

    # Initialize 2D array to hold sub-images
    sub_images = np.empty((rows, cols), dtype=object)

    # Split image into sub-images and store in 2D array
    for i in range(rows):
        for j in range(cols):
            sub_image = img_array[i*size:(i+1)*size, j*size:(j+1)*size]
            sub_images[i][j] = sub_image

    # Return 2D array of sub-images
    return sub_images, cols

from PIL import Image
import numpy as np

def combine_images(sub_images):
    sub_image_size = sub_images[0][0].size[1]
    num_rows, num_cols = len(sub_images), len(sub_images[0])
    combined_image = Image.new('RGB', (num_cols * sub_image_size, num_rows * sub_image_size))

    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            sub_image = sub_images[row_idx][col_idx]
            combined_image.paste(sub_image, (col_idx * sub_image_size, row_idx * sub_image_size))

    return combined_image








