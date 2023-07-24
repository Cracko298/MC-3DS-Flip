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


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: .\m3dsflip <mode> <command> <image_path>")
        sys.exit(1)
    
    flip_direction = sys.argv[1].lower()
    
    xflip = True if flip_direction == "xflip" else False
    yflip = True if flip_direction == "yflip" else False
    dstflip = True if flip_direction == "3dstflip" else False
    filter_contrast = True if flip_direction == '-c' else False
    grab_content = True if flip_direction == '-g' else False

    if yflip == True or xflip == True or dstflip == True:
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

        if content == '-meta':
            if '.3dst' not in image_path:
                print("Provided File is Not in *.3DST Format.")
            else:
                meta_grab(image_path)
        exit(1)

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