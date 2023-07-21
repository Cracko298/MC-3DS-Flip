import sys
from PIL import Image
from tqdm import tqdm

def is_minecraft_skin(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size

        if width == 64 and height == 64:

            if image.mode == "RGBA":
                pixel = image.getpixel((0, 0))

                if pixel[3] == 0:
                    return True
                
    except IOError:
        pass

    return False

def flip_image(image_path, xflip=False, yflip=False):
    image = Image.open(image_path)
    
    if xflip:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    if yflip:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    
    flipped_image_path = f"flipped_{image_path}"
    
    progress_bar = tqdm(total=100, desc="Flipping Image", unit="%", ncols=80)
    
    for i in range(1000):

        progress_bar.update(1)
        progress_bar.set_postfix({"Progress": f"{i}%"})
    
    progress_bar.close()
    
    image.save(flipped_image_path)
    print(f"Flipped image saved as: '{flipped_image_path}'")

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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: .\m3dsflip <mode> <command> <image_path>")
        sys.exit(1)
    
    flip_direction = sys.argv[1].lower()
    
    xflip = True if flip_direction == "xflip" else False
    yflip = True if flip_direction == "yflip" else False
    dstflip = True if flip_direction == "3dstflip" else False
    filter_contrast = True if flip_direction == '-c' else False

    if yflip == True or xflip == True or dstflip == True:
        image_path = sys.argv[2]
    
    if flip_direction == '-c':
        image_path = sys.argv[3]
        color = sys.argv[2]

        if color == '-invert':
            invert(image_path)
        elif color == '-green':
            green(image_path)
    



    offset = 0x20

    if dstflip == True:
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

    else:
        if not is_minecraft_skin(image_path):
            print("The provided image is not a Minecraft skin.")
            print(" ")
            sys.exit(1)
        
        flip_image(image_path, xflip, yflip)
