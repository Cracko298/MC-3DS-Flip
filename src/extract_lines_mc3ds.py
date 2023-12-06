from PIL import Image
import array

image_path = "gingy.3dst"

def reverse_four_bytes(data):
    reversed_four_bytes = data[:4][::-1]
    return reversed_four_bytes

def reverse_three_bytes(data):
    reversed_three_bytes = data[:3][::-1]
    reversed_three_bytes += data[3:4]
    return reversed_three_bytes

with open(image_path, 'rb') as file:
    out_path = image_path.replace(".3dst", "_firstline.3dst")
    print("1")
    file.seek(0x20, 1)

    with open(out_path, 'wb+') as f:
        print("2")
        for _ in range(8):
            data1 = file.read(0x08)
            print(data1)
            file.seek(0x08, 1)
            data2 = file.read(0x08)
            file.seek(0x28, 1)
            data3 = file.read(0x08)
            file.seek(0x08, 1)
            data4 = file.read(0x08)
            file.seek(0xA8, 1)
            f.write(data1)
            f.write(data2)
            f.write(data3)
            f.write(data4)

output_file_path = 'outp_img.png'
with open("converted_files.r3dst",'wb+') as f:
    with open(out_path, 'rb') as file:
        for i in range(0x01, 0x41):
            data = file.read(0x04)

            data = reverse_four_bytes(data)
            data = reverse_three_bytes(data)

            f.write(data)
            file.seek(0x04 * i)