import os
from PIL import Image

def parse_argb_data(filename):
    with open(filename, "rb") as file:
        # Skip the first 0x20 bytes as the offset
        file.seek(0x20)
        data = file.read()

    # Assuming the data is in 8x8 blocks, calculate the image width and height.
    block_width = 8
    block_height = 8

    # Calculate the number of blocks along the width of the image
    num_blocks_width = 64 // block_width
    image_width = block_width * num_blocks_width
    image_height = block_height * 8

    # Extract ARGB values from the data.
    pixels = []
    for i in range(0, len(data), 4):
        alpha = data[i]
        red = data[i + 1]
        green = data[i + 2]
        blue = data[i + 3]
        pixels.append((red, green, blue, alpha))

    return pixels, image_width, image_height

def create_png_image(pixels, width, height, output_filename):
    image = Image.new("RGBA", (width, height))
    
    # Use putpixel() to set individual pixels in the image
    for block_y in range(0, height, 8):
        for block_x in range(0, width, 8):
            block_index = (block_y // 8) * (width // 8) + (block_x // 8)
            for y in range(8):
                for x in range(8):
                    pixel_index = block_index * 64 + y * 8 + x
                    image_x = block_x + x
                    image_y = block_y + y
                    image.putpixel((image_x, image_y), pixels[pixel_index])

    image.save(output_filename)

def main():
    input_filename = "gingerbread.3dst"
    output_filename = "gingerbread.png"

    pixels, image_width, image_height = parse_argb_data(input_filename)
    create_png_image(pixels, image_width, image_height, output_filename)

    print("PNG image saved as:", output_filename)

if __name__ == "__main__":
    main()
