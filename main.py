import os
import pickle
from PIL import Image
import numpy as np
from skimage import io

def get_avg_color(image):
    img = io.imread(image)
    img = img.astype(np.float32) / 255.0  # Normalize pixel values to the range [0, 1]
    avg_color = np.mean(img, axis=(0,1))
    avg_color = avg_color[:3]  # Take the first three elements of avg_color
    return avg_color

  
# Define the directory where the images are stored
image_dir = "blocks"

# Check if the average color data file exists
data_file = "average_colors.pkl"
if os.path.isfile(data_file):
    # If the data file exists, load the average color data
    with open(data_file, "rb") as f:
        avg_colors = pickle.load(f)
else:
    # If the data file does not exist, calculate the average color of each image and save the data
    images = os.listdir(image_dir)
    avg_colors = {}
    for image in images:
        avg_color = get_avg_color(os.path.join(image_dir, image))
        avg_colors[image] = avg_color
    with open(data_file, "wb") as f:
        pickle.dump(avg_colors, f)

# Calculate the average color of the query image
query_image = "yes.png"
query_color = get_avg_color(query_image)

# Compare the average color of the query image to the average colors of the other images
distances = {}
for image, avg_color in avg_colors.items():
    dist = np.linalg.norm(query_color - avg_color)
    distances[image] = dist
    print('avg_color shape for', image, ':', avg_color.shape)


# Find the filename of the image with the closest average color
closest_image = min(distances, key=distances.get)

print(closest_image)