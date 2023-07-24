def grab_meta(image_path):
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

        print(" ")
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


image_path = 'flipped_gingerbread.3dst'
grab_meta(image_path)