# Minecraft Image Builder

This program allows you to select an image and build it in Minecraft using blocks. It is designed for the Bedrock Edition of Minecraft.

## Prerequisites

Before running the program, ensure that you have the following installed:

- Python 3.x
- tkinter
- PIL (Python Imaging Library)

## Installation

1. Clone the repository to your local machine:

   ```bash
   $ git clone https://github.com/geosage/MCBE-ImageToBlocks.git
   ```
2. Install the required dependencies:

   ```bash
   $ pip install tkinter pillow
   ```

## Usage
1. Run the main.py script:

   ```bash
   $ python main.py
   ```
2. A file dialog will appear, allowing you to select an image (supports .jpg, .png, .gif, .bmp). Choose an image and click "Open".

3. The selected image will be resized and saved as mainimage.png. The program will display a success message if the image is uploaded successfully.

4. The program will split the image into smaller blocks for processing and print the number of images being processed.

5. The closest images to the processed blocks will be selected and combined to create the final image. The combined image will be saved as finalimage.jpg.

6. The finalimage.jpg file will be opened automatically.

7. You will be prompted to import the final image into your Minecraft world. Respond with "Yes" or "No". If you choose "Yes", the program will proceed with the import process; otherwise, it will exit.

## Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the repository.

## License
This project is licensed under the BSD 3-Clause License.

## Contact Information
For any further questions or inquiries, please contact "groego" on discord.
