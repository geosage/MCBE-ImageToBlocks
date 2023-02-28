import os
import pickle
import numpy as np
from PIL import Image

def get_avg_color(image):
    img = np.array(image)
    img = img.astype(np.float32) / 255.0  # Normalize pixel values to the range [0, 1]
    avg_color = np.mean(img, axis=(0, 1))
    avg_color = avg_color[:3]  # Take the first three elements of avg_color
    return avg_color

def get_closest_image(imagestoprocess):
    blocks_dir = 'blocks'

    # Check if the average color data file exists
    data_file = os.path.join(blocks_dir, "average_colors.pkl")
    if os.path.isfile(data_file):
        # If the data file exists, load the average color data
        with open(data_file, "rb") as f:
            avg_colors = pickle.load(f)
    else:
        # If the data file does not exist, calculate the average color of each image and save the data
        images = os.listdir(blocks_dir)
        avg_colors = {}
        for image in images:
            img = Image.open(os.path.join(blocks_dir, image))
            avg_color = get_avg_color(img)
            avg_colors[image] = avg_color
            img.close()  # Close the file

        with open(data_file, "wb") as f:
            pickle.dump(avg_colors, f)

    processed_images = []
    for image in imagestoprocess:
        # Convert the query image from a list to a NumPy array
        query_image = np.array(image, dtype=np.uint8)

        # Convert the NumPy array to a PIL Image object
        query_image = Image.fromarray(query_image)

        # Calculate the average color of the query image
        query_color = get_avg_color(query_image)

        # Compare the average color of the query image to the average colors of the other images
        distances = {}
        for image_name, avg_color in avg_colors.items():
            dist = np.linalg.norm(query_color - avg_color)
            distances[image_name] = dist

        # Find the filename of the image with the closest average color
        closest_image = min(distances, key=distances.get)

        # Replace the query image with the closest image
        processed_images.append(Image.open(os.path.join(blocks_dir, closest_image)))


    return processed_images