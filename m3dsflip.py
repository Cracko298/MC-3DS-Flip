import sys
from PIL import Image
from tqdm import tqdm

def is_minecraft_skin(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size

        if width == 64 and height == 32 or width == 64 and height == 64:

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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: .\m3dsflip.exe <command> <image_path>")
        sys.exit(1)
    
    flip_direction = sys.argv[1].lower()
    image_path = sys.argv[2]

    if not is_minecraft_skin(image_path):
        print("The provided image is not a Minecraft skin.")
        print(" ")
        sys.exit(1)
    
    xflip = True if flip_direction == "xflip" else False
    yflip = True if flip_direction == "yflip" else False
    
    flip_image(image_path, xflip, yflip)
