from PIL import Image

def imagesize():
    filepath = "yes.jpg"
    img = Image.open(filepath)
    width = img.width
    height = img.height
    return height, width

imagesize()

print(height + width)
