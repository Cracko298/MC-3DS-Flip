import imageio

def flip_image_over_x_axis(input_file, output_file):
    image = imageio.imread(input_file)
    flipped_image = image[::1, ::-1]
    imageio.imwrite(output_file, flipped_image)

# Vars and Call
input_filename = "alex.png"
output_filename = "outpsssut.png"
flip_image_over_x_axis(input_filename, output_filename)
