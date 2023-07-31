from PIL import Image

def extract_pixel_data(image, x, y, size):
    pixel_data = []
    for dy in range(size):
        for dx in range(size):
            if x + dx < image.width and y + dy < image.height:
                pixel = image.getpixel((x + dx, y + dy))
                pixel_data.extend(pixel)
            else:
                # If the image size is not perfectly divisible by the specified size, handle the remaining pixels.
                pixel_data.extend([0, 0, 0, 0])  # Add transparent black pixel (RGBA format)
    return bytes(pixel_data)


def process_image(image_path, output_file, section_size):
    try:
        image = Image.open(image_path)

        with open(output_file, 'wb') as output:
            for y in range(0, image.height, section_size):
                for x in range(0, image.width, section_size):
                    pixel_data = extract_pixel_data(image, x, y, section_size)
                    output.write(pixel_data)

        print("Image processing and writing to the file completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = "gingy.png"
    output_file = "gingy.3dst"
    section_size = 8
    process_image(image_path, output_file, section_size)
