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





def dst_flip(image_path, offset):
    data_list = []
    with open(image_path, 'rb') as file:
        # Move the file pointer to the specified offset
        file.seek(offset)
        
        while True:
            # Read 16 bytes from the file
            data = file.read(16)
            if not data:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list.append(data)
    
    return data_list





if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: .\m3dsflip.exe <command> <image_path>")
        sys.exit(1)
    
    flip_direction = sys.argv[1].lower()
    image_path = sys.argv[2]
    
    xflip = True if flip_direction == "xflip" else False
    yflip = True if flip_direction == "yflip" else False
    dstflip = True if flip_direction == "3dstflip" else False
    offset = 0x20

    if  dstflip == True:
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


    else:
        if not is_minecraft_skin(image_path):
            print("The provided image is not a Minecraft skin.")
            print(" ")
            sys.exit(1)
        
        flip_image(image_path, xflip, yflip)
