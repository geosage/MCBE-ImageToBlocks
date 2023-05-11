import os
import pickle
import numpy as np
from PIL import Image

def get_avg_color(image):
    img = np.array(image)
    img = img.astype(np.float32) / 255.0  # Normalize pixel values to the range [0, 1]
    avg_color = np.mean(img, axis=(0, 1))
    if isinstance(avg_color, np.ndarray):
        avg_color = avg_color[:3]  # Take the first three elements of avg_color
    else:
        avg_color = np.array([avg_color, avg_color, avg_color])  # Create a numpy array with three identical elements
    return avg_color

def get_closest_image(imagestoprocess):
    b = 1
    blocks_dir = 'blocks'

    # Check if the average color data file exists
    data_file = os.path.join(blocks_dir, "average_colors.pkl")
    if os.path.isfile(data_file):
        # If the data file exists, load the average color data
        with open(data_file, "rb", buffering=1024*1024) as f:
            avg_colors = pickle.load(f)
    else:
        # If the data file does not exist, calculate the average color of each image and save the data
        images = os.listdir(blocks_dir)
        avg_colors = {}
        for i, image in enumerate(images):
            img = Image.open(os.path.join(blocks_dir, image))
            avg_color = get_avg_color(img)
            avg_colors[image] = avg_color
            img.close()  # Close the file after processing

        if (i + 1) % len(images) == 0:
            with open(data_file, "wb", buffering=1024*1024) as f:
                pickle.dump(avg_colors, f)
            avg_colors = {}

    imagenames = []
    processed_images = []
    for row in imagestoprocess:
        row_images = []
        for image in row:
            # Convert the query image from a list to a NumPy array
            query_image = np.array(image, dtype=np.uint8)

            # Convert the NumPy array to a PIL Image object
            query_image = Image.fromarray(query_image)

            # Calculate the average color of the query image
            query_color = get_avg_color(query_image)

            #Compare the average color of the query image to the average colors of the other images
            distances = {}
            for image_name, avg_color in avg_colors.items():
                dist = np.linalg.norm(query_color - avg_color)
                distances[image_name] = dist

            # Find the filename of the image with the closest average color
            closest_image = min(distances, key=distances.get)
            imagenames.append(closest_image)

            # Replace the query image with the closest image
            with Image.open(os.path.join(blocks_dir, closest_image)) as closest_img:
                row_images.append(closest_img.copy())

            #BASICALLY THIS CODE ^^^^^ NEEDS THE IMAGES... THE REST OF IT DOESNT!

            # Close the query image
            query_image.close()


        processed_images.append(row_images)
        if b % 7 == 0:
            print("Processed " + str(b) + "/" + str(len(imagestoprocess)) + " Rows")
        b += 1
    print("Processed " + str(b-1) + "/" + str(len(imagestoprocess)) + " Rows")
    print("Finished!, Yup")
    return processed_images, imagenames