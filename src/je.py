import numpy as np
from PIL import Image

# Define image dimensions
width = 64
height = 8

# Read the raw data from the file
with open("gingy.3dst", "rb") as file:
    file.seek(32)  # Skip the initial offset
    raw_data = file.read()

# Split the raw data into chunks of 2048 bytes
chunks = [raw_data[i:i + 2048] for i in range(0, len(raw_data), 2048)]

# Initialize an empty array to store pixel data
pixel_data = np.zeros((height, width, 4), dtype=np.uint8)

# Convert raw data to ARGB format and populate pixel data array
for chunk_index, chunk in enumerate(chunks):
    for pixel_index in range(0, len(chunk), 4):
        argb = chunk[pixel_index:pixel_index + 4]
        alpha, red, green, blue = argb
        pixel_data[chunk_index, pixel_index // 4] = [red, green, blue, alpha]  # Swap alpha and red

# Create and save images from pixel data
for image_index in range(height):
    image = Image.fromarray(pixel_data[image_index])
    image.save(f"image_{image_index + 1}.png")

print("Images saved successfully.")
