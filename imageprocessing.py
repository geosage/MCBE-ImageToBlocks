from PIL import Image
import math

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

def split_image(image_path, block_size):
    with Image.open(image_path) as img:
        width, height = img.size
        images = []
        for x in range(0, width, block_size):
            for y in range(0, height, block_size):
                box = (y, x, y+block_size, x+block_size)
                images.append(img.crop(box))
    return images

def combine_images(images, block_size):
    num_images = len(images)
    rows = int(math.ceil(math.sqrt(num_images)))
    cols = int(math.ceil(num_images / rows))
    width = cols * block_size
    height = rows * block_size

    new_image = Image.new('RGB', (width, height), (255, 255, 255, 0))

    for i, image in enumerate(images):
        x = (i % cols) * block_size
        y = (i // cols) * block_size
        new_image.paste(image, (x, y))

    return new_image
