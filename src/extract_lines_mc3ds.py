import sys

image_path = sys.argv[1]

def reverse_four_bytes(data):
    reversed_four_bytes = data[:4][::-1]
    return reversed_four_bytes

def reverse_three_bytes(data):
    reversed_three_bytes = data[:3][::-1]
    reversed_three_bytes += data[3:4]
    return reversed_three_bytes

if ".3dst" not in image_path:
    print('Error: Provided File is not a Valid .3dst Image.\n')
    sys.exit(1)

with open(image_path, 'rb') as file:
    header_data = file.read(0x20)
    out_path = image_path.replace(".3dst", "_firstline.3dst")
    print("1")
    file.seek(0x20, 1)

    with open(out_path, 'wb+') as f:
        f.write(header_data)
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

with open(f"{image_path}_converted.r3dst",'wb+') as f:
    with open(out_path, 'rb') as file:
        file.seek(0x20, 1)
        for i in range(0x01, 0x41):
            data = file.read(0x04)
            data = reverse_four_bytes(data)
            data = reverse_three_bytes(data)

            f.write(data)
            file.seek(0x04 * i)