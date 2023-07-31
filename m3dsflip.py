import sys
from PIL import Image

def yaxis_flip(image_path, output_path):
    image = Image.open(image_path)
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_image.save(f"{output_path}")
    print(f"Saved Image As: {output_path}")



def xaxis_flip(image_path, output_path):
    image = Image.open(image_path)
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_image.save(f"{output_path}")
    print(f"Saved Image As: {output_path}")



def green_filter(rgb_bytes):
    red = rgb_bytes[0]
    green = rgb_bytes[1]
    blue = rgb_bytes[2]

    if red >= 0x10:
        red -= 0x10

    if blue >= 0x10:
        blue -= 0x10
    
    green = 0xB0

    green_filtered_rgb = bytearray([red, green, blue])
    return green_filtered_rgb

def green(image_path):
    with open(image_path, 'rb+') as file:
        while True:
            offset = file.tell()
            byte = file.read(1)

            if not byte:
                break

            if offset >= 0x20 and byte == b'\xFF':
                rgb_bytes = file.read(3)
                if len(rgb_bytes) == 3:
                    green_filtered_rgb = green_filter(rgb_bytes)
                    file.seek(-3, 1)
                    file.write(green_filtered_rgb)
    
    print(f"Set Green Hue To: '{image_path}'.")

def dst_flip(image_path, offset):
    data_list = []
    with open(image_path, 'rb') as file:
        file.seek(offset)
        
        while True:
            data = file.read(16)
            if not data:
                break
            
            data_list.append(data)
    
    return data_list


def invert_color(rgb_bytes):
    inverted_rgb = bytearray([255 - byte for byte in rgb_bytes])
    return inverted_rgb

def invert(image_path):
    with open(image_path, 'rb+') as file:
        while True:
            offset = file.tell()
            byte = file.read(1)

            if not byte:
                break

            if offset >= 0x20 and byte == b'\xFF':
                rgb_bytes = file.read(3)
                if len(rgb_bytes) == 3:
                    inverted_rgb = invert_color(rgb_bytes)
                    file.seek(-3, 1)
                    file.write(inverted_rgb)
    
    print(f"Inverted Color of: '{image_path}'.")

def red_filter(rgb_bytes):
    red = rgb_bytes[0]
    green = rgb_bytes[1]
    blue = rgb_bytes[2]

    if red >= 0x10:
        red -= 0x10

    blue = 0xA0

    if green >= 0x10:
        green -= 0x10

    red_filter_bytes = bytearray([red, green, blue])
    return red_filter_bytes

def red(image_path):
    with open(image_path, 'rb+') as file:
        while True:
            offset = file.tell()
            byte = file.read(1)

            if not byte:
                break

            if offset >= 0x20 and byte == b'\xFF':
                rgb_bytes = file.read(3)
                if len(rgb_bytes) == 3:
                    red_filter_bytes = red_filter(rgb_bytes)
                    file.seek(-3, 1)
                    file.write(red_filter_bytes)
    
    print(f"Set Red Hue To: '{image_path}'.")

def orange_filter(rgb_bytes):
    red = rgb_bytes[0]
    green = rgb_bytes[1]
    blue = rgb_bytes[2]

    red = 0x10

    blue = 0xF0

    orange_filter_rgb = bytearray([red, green, blue])
    return orange_filter_rgb

def orange(image_path):
    with open(image_path, 'rb+') as file:
        while True:
            offset = file.tell()
            byte = file.read(1)

            if not byte:
                break

            if offset >= 0x20 and byte == b'\xFF':
                rgb_bytes = file.read(3)
                if len(rgb_bytes) == 3:
                    orange_filter_rgb = orange_filter(rgb_bytes)
                    file.seek(-3, 1)
                    file.write(orange_filter_rgb)
    
    print(f"Set Orange/Yellow Hue To: '{image_path}'.")



def blue_filter(rgb_bytes):
    red = rgb_bytes[0]
    green = rgb_bytes[1]
    blue = rgb_bytes[2]

    red = 0xDF

    green = 0xFF

    blue_filter_rgb = bytearray([red, green, blue])
    return blue_filter_rgb

def blue(image_path):
    with open(image_path, 'rb+') as file:
        while True:
            offset = file.tell()
            byte = file.read(1)

            if not byte:
                break

            if offset >= 0x20 and byte == b'\xFF':
                rgb_bytes = file.read(3)
                if len(rgb_bytes) == 3:
                    blue_filter_rgb = blue_filter(rgb_bytes)
                    file.seek(-3, 1)
                    file.write(blue_filter_rgb)
    
    print(f"Set Blue Hue To: '{image_path}'.")


def meta_grab(image_path):
    tempdata = image_path.replace('.3dst','')
    output_path = f"{tempdata}_metadata.txt"
    with open(image_path, 'rb') as f, open(output_path, 'a') as of:
        data0 = f.read(0x4)
        f.seek(0x4)
        data1 = f.read(0x01)
        f.seek(0xC)
        data2 = f.read(0x01)
        f.seek(0x10)
        data3 = f.read(0x01)
        f.seek(0x14)
        data4 = f.read(0x01)
        f.seek(0x18)
        data5 = f.read(0x01)

        int_data = int.from_bytes(data1)
        print(f"Texture Mode: {int_data}")
        of.write(f"Texture Mode: {int_data}\n")
        int_data = int.from_bytes(data2)
        print(f"Skin Width: {int_data}")
        of.write(f"Skin Width: {int_data}\n")
        int_data = int.from_bytes(data3)
        print(f"Skin Height: {int_data}")
        of.write(f"Skin Height: {int_data}\n")

        int_data = data0.decode("ascii")
        print(f"Header Name: {int_data}")
        of.write(f"Header Name: {int_data}\n")
        print(f'MIP Value: 1')
        of.write(f"MIP Value: 1\n")
        print("Img Format: RGBA8")
        of.write(f"Image Format: RGBA8\n")
        print("Bit Depth: 8")
        of.write(f"Bit Depth: 8\n")

        int_data = int.from_bytes(data4)
        print(f"Width Checksum: {int_data}")
        of.write(f"Width Checksum: {int_data}\n")
        int_data = int.from_bytes(data5)
        print(f"Height Checksum: {int_data}")
        of.write(f"Height Checksum: {int_data}\n")
        print(" ")
        print(f"Saved MetaData As: '{output_path}'.")
        sys.exit(1)

def grab_png_head(image_path, output_path):
    image = Image.open(image_path)
    x_coor, y_coor, x1, y1 = (0, 48, 32, 64)
    grab_head = image.crop((x_coor, y_coor, x1, y1))
    grab_head.save(output_path)
    print(f"Saved Head Image As: '{output_path}'.")
    sys.exit(1)

def grab_png_body(image_path, output_path):
    image = Image.open(image_path)
    x_coor, y_coor, x1, y1 = (16, 32, 40, 48)
    grab_body = image.crop((x_coor, y_coor, x1, y1))
    grab_body.save(output_path)
    print(f"Saved Body Image As: '{output_path}'.")
    sys.exit(1)

def grab_png_larm(image_path, output_path):
    image = Image.open(image_path)
    x_coor, y_coor, x1, y1 = (32, 0, 46, 16)
    grab_body = image.crop((x_coor, y_coor, x1, y1))
    grab_body.save(output_path)
    print(f"Saved Left Arm Image As: '{output_path}'.")
    sys.exit(1)

def grab_png_rarm(image_path, output_path):
    image = Image.open(image_path)
    x_coor, y_coor, x1, y1 = (40, 32, 58, 48)
    grab_body = image.crop((x_coor, y_coor, x1, y1))
    grab_body.save(output_path)
    print(f"Saved Right Arm Image As: '{output_path}'.")
    sys.exit(1)

def grab_png_lleg(image_path, output_path):
    image = Image.open(image_path)
    x_coor, y_coor, x1, y1 = (16, 0, 32, 16)
    grab_body = image.crop((x_coor, y_coor, x1, y1))
    grab_body.save(output_path)
    print(f"Saved Left Leg Image As: '{output_path}'.")
    sys.exit(1)

def grab_png_rleg(image_path, output_path):
    image = Image.open(image_path)
    x_coor, y_coor, x1, y1 = (0, 32, 16, 48)
    grab_body = image.crop((x_coor, y_coor, x1, y1))
    grab_body.save(output_path)
    print(f"Saved Right Leg Image As: '{output_path}'.")
    sys.exit(1)

def grab_3dst_head(image_path, output_path):
    offset = 0x20
    with open(image_path,'rb') as f, open(output_path, 'rb+') as outpf:
        header = f.read(offset)
        f.seek(0x3020)
        data = f.read(0x4020-0x3020)


        outpf.write(header)
        outpf.seek(offset)
        outpf.write(data)
        sys.exit(1)


def extract_pixel_data(image, x, y, size):
    pixel_data = []
    for dy in range(size):
        for dx in range(size):
            if x + dx < image.width and y + dy < image.height:
                pixel = image.getpixel((x + dx, y + dy))
                pixel_data.extend(pixel)
            else:
                pixel_data.extend([0, 0, 0, 0])
    return bytes(pixel_data)


def process_image(image_path, output_file, section_size):
    try:
        image = Image.open(image_path)

        with open(output_file, 'wb') as output:
            for y in range(0, image.height, section_size):
                for x in range(0, image.width, section_size):
                    pixel_data = extract_pixel_data(image, x, y, section_size)
                    output.write(pixel_data)

        print(f"Converted 3DST Image '{image_path}' to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_argb_data(filename, output_path):
    with open(filename, "rb") as file:
        file.seek(0x20)
        data = file.read()

    block_width = 8
    block_height = 8

    num_blocks_width = 64 // block_width
    image_width = block_width * num_blocks_width
    image_height = block_height * 8

    pixels = []
    for i in range(0, len(data), 4):
        alpha = data[i]
        red = data[i + 1]
        green = data[i + 2]
        blue = data[i + 3]
        pixels.append((red, green, blue, alpha))
        


    create_png_image(pixels, image_width, image_height, output_path, filename)

def create_png_image(pixels, width, height, output_filename, filename):
    image = Image.new("RGBA", (width, height))

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
    print(f"Converted PNG Image '{filename}' to '{output_filename}'.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: .\m3dsflip <flag> <command> <image_path>")
        print("Helpful Hint: Simple Commands don't require a Flag.")
        sys.exit(1)
    
    flip_direction = sys.argv[1].lower()
    
    xflip = True if flip_direction == "xflip" else False
    yflip = True if flip_direction == "yflip" else False
    dstflip = True if flip_direction == "3dstflip" else False
    filter_contrast = True if flip_direction == '-c' else False
    grab_content = True if flip_direction == '-g' else False
    convert = True if flip_direction == '-con' else False

    if yflip == True or xflip == True or dstflip == True or convert == True:
        image_path = sys.argv[2]
    
    if filter_contrast == True:
        image_path = sys.argv[3]
        color = sys.argv[2]

        if color == '-invert':
            invert(image_path)
        elif color == '-green':
            green(image_path)
        elif color == '-orange':
            orange(image_path)
        elif color == '-red':
            red(image_path)
        elif color == '-blue':
            blue(image_path)

    if grab_content == True:
        image_path = sys.argv[3]
        content = sys.argv[2]

        if '.3dst' in image_path:
            chk0 = ['-meta','-head']

            if content == '-meta':
                meta_grab(image_path)

            if content == '-head':
                output_path = f'head_export_{image_path}'
                grab_3dst_head(image_path, output_path)

            if content not in chk0:
                print(f"Argument '{content}' is Not Supported.")
                print("Reminder: 'Commands/Flags/Args' are case-sensitive.")

            sys.exit(1)

        elif 'png' in image_path:

            if content == '-head':
                output_path = f'_head_export_{image_path}'
                grab_png_head(image_path, output_path)

            if content == '-body':
                output_path = f'_body_export_{image_path}'
                grab_png_body(image_path, output_path)

            if content == '-larm':
                output_path = f'_lArm_export_{image_path}'
                grab_png_larm(image_path, output_path)

            if content == '-rarm':
                output_path = f'_rArm_export_{image_path}'
                grab_png_rarm(image_path, output_path)

            if content == '-lleg':
                output_path = f'_Lleg_export_{image_path}'
                grab_png_lleg(image_path, output_path)

            if content == '-rleg':
                output_path = f'_Rleg_export_{image_path}'
                grab_png_rleg(image_path, output_path)

            sys.exit(1)

        else:
            print(f"Image/File '{image_path}' is Not Supported.")
            sys.exit(1)

    if convert == True:
        if '.png' in image_path:
            output_path = f'New_p23_{image_path}'
            section_size = 8
            process_image(image_path, output_path, section_size)

        elif '.3dst' in image_path:
            output_path = f"New_32p_{image_path}"
            parse_argb_data(image_path, output_path)
            
        else:
            print(f"Image/File '{image_path}' is Not Supported.")
            sys.exit(1)
        
        sys.exit(1)

    offset = 0x20
    if yflip == True:
        output_path = f"y_flipped_{image_path}"
        
        if '.3dst' in image_path:
            print("Provided File is Not in *.PNG Format.")
        else:
            yaxis_flip(image_path, output_path)

    if xflip == True:
        output_path = f"x_flipped_{image_path}"

        if '.3dst' in image_path:
            print("Provided File is Not in *.PNG Format.")
        else:
            xaxis_flip(image_path, output_path)

    if dstflip == True:

        if '.3dst' not in image_path:
            print("Provided File is Not in *.3DST Format.")
        else:
            pass


        data_blocks = dst_flip(image_path, offset)
    
        # Store each 16-byte block in separate variables
        num_blocks = len(data_blocks)
        for i, data_block in enumerate(data_blocks):
            var_name = f"data_block_{i}"
            print(f"16-Byte Block: {var_name}")
            globals()[var_name] = data_block

        
        with open(image_path, 'rb') as file:
            header = file.read(offset)

        with open(f"flipped_{image_path}", 'wb') as file0:
            file0.write(header)

            for i in range(1024):
                number0 = 1023 - i

                var_name = f"data_block_{number0}"
                data_block = globals()[var_name]

                # Write the data_block to the file
                file0.write(data_block)
        
        print(f"Flipped 3DST Saved As: 'generated_{image_path}'")
        sys.exit(1)

    elif flip_direction == '-c':
        sys.exit(1)