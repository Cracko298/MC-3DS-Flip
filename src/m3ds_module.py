import os

number = 0

def chunks_write(tmp0, tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7, tmp8, header, out_path, temp_path, temp0_path):
    data_list1 = []
    with open(tmp0, 'rb') as file:
        while True:
            # Read 16 bytes from the file
            data = file.read(16)
            if not data:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list1.append(data)

    data_list2 = []
    with open(tmp1, 'rb') as file:
        while True:
            # Read 16 bytes from the file
            data1 = file.read(16)
            if not data1:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list2.append(data1)

    data_list3 = []
    with open(tmp2, 'rb') as file:
        while True:
            # Read 16 bytes from the file
            data1 = file.read(16)
            if not data1:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list3.append(data1)
    
    data_list4 = []
    with open(tmp3, 'rb') as file:
        while True:
            # Read 16 bytes from the file
            data1 = file.read(16)
            if not data1:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list4.append(data1)
    
    data_list5 = []
    with open(tmp4, 'rb') as file:
        while True:
            # Read 16 bytes from the file
            data1 = file.read(16)
            if not data1:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list5.append(data1)
    
    data_list6 = []
    with open(tmp5, 'rb') as file:
        while True:
            # Read 16 bytes from the file
            data1 = file.read(16)
            if not data1:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list6.append(data1)
    
    data_list7 = []
    with open(tmp6, 'rb') as file:
        while True:
            # Read 16 bytes from the file
            data1 = file.read(16)
            if not data1:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list7.append(data1)
    
    
    data_list8 = []
    with open(tmp7, 'rb') as file:
        while True:
            # Read 16 bytes from the file
            data1 = file.read(16)
            if not data1:
                break  # End of file
            
            # Store the data in a list as bytes
            data_list8.append(data1)
    
    
    if data_list1 is not None and data_list2 is not None:

        for i, data_block in enumerate(data_list1):
            var_name = f"data1_block_{i}"
            print(var_name)
            globals()[var_name] = data_block

        for a, data_block1 in enumerate(data_list2):
            var_name = f"data2_block_{a}"
            print(var_name)
            globals()[var_name] = data_block1

        for i, data_block in enumerate(data_list3):
            var_name = f"data3_block_{i}"
            print(var_name)
            globals()[var_name] = data_block

        for a, data_block1 in enumerate(data_list4):
            var_name = f"data4_block_{a}"
            print(var_name)
            globals()[var_name] = data_block1

        for i, data_block in enumerate(data_list5):
            var_name = f"data5_block_{i}"
            print(var_name)
            globals()[var_name] = data_block

        for a, data_block1 in enumerate(data_list6):
            var_name = f"data6_block_{a}"
            print(var_name)
            globals()[var_name] = data_block1

        for i, data_block in enumerate(data_list7):
            var_name = f"data7_block_{i}"
            print(var_name)
            globals()[var_name] = data_block

        for a, data_block1 in enumerate(data_list8):
            var_name = f"data8_block_{a}"
            print(var_name)
            globals()[var_name] = data_block1

        with open(out_path, 'wb') as file0:
            file0.write(header)

            for i in range(1, 127):
                number0 = 128 - i
                var_name = f"data8_block_{number0}"
                data_block = globals()[var_name]
                file0.write(data_block)

            for i in range(1, 128):
                number0 = 128 - i
                var_name = f"data7_block_{number0}"
                data_block = globals()[var_name]
                file0.write(data_block)

            for i in range(1, 128):
                number0 = 128 - i
                var_name = f"data6_block_{number0}"
                data_block = globals()[var_name]
                file0.write(data_block)

            for i in range(1, 128):
                number0 = 128 - i
                var_name = f"data5_block_{number0}"
                data_block = globals()[var_name]
                file0.write(data_block)

            for i in range(1, 128):
                number0 = 128 - i
                var_name = f"data4_block_{number0}"
                data_block = globals()[var_name]
                file0.write(data_block)

            for i in range(1, 128):
                number0 = 128 - i
                var_name = f"data3_block_{number0}"
                data_block = globals()[var_name]
                file0.write(data_block)
        
            for i in range(1, 128):
                number0 = 128 - i
                var_name = f"data2_block_{number0}"
                data_block = globals()[var_name]
                file0.write(data_block)

            for i in range(1, 128):
                number0 = 128 - i
                var_name = f"data1_block_{number0}"
                data_block = globals()[var_name]
                file0.write(data_block)

    os.remove(temp_path)

    for i in range(8):
        os.remove(f"{i}_{temp0_path}")





def yaxis_flip_3dst(image_path):
    temp0_path = image_path.replace('.3dst','.tmpdata')
    temp_path = f"1_temp_{temp0_path}"

    tmp0 = f"0_{temp0_path}"
    tmp1 = f"1_{temp0_path}"
    tmp2 = f"2_{temp0_path}"
    tmp3 = f"3_{temp0_path}"
    tmp4 = f"4_{temp0_path}"
    tmp5 = f"5_{temp0_path}"
    tmp6 = f"6_{temp0_path}"
    tmp7 = f"7_{temp0_path}"
    tmp8 = f"8_{temp0_path}"

    out_path = f"flipped_{image_path}"

    with open(image_path, 'rb') as file:
        header = file.read(0x20)
        file.seek(0x20)
        dst_data = file.read()

    with open(temp_path, 'wb') as file0:
        file0.write(dst_data)

    with open(temp_path, 'rb') as file1:
        first_q = file1.read(0x800)
        file1.seek(0x1000)
        second_q = file1.read(0x800)
        file1.seek(0x1800)
        third_q = file1.read(0x800)
        file1.seek(0x2000)
        forth_q = file1.read(0x800)
        file1.seek(0x2800)
        fifth_q = file1.read(0x800)
        file1.seek(0x3000)
        sixth_q = file1.read(0x800)
        file1.seek(0x3800)
        seventh_q = file1.read(0x800)

        with open(tmp0, 'wb') as f0:
            with open(tmp1, 'wb') as f1:
                with open(tmp2, 'wb') as f2:
                    with open(tmp3, 'wb') as f3:
                        with open(tmp4, 'wb') as f4:
                            with open(tmp5, 'wb') as f5:
                                with open(tmp6, 'wb') as f6:
                                    with open(tmp7, 'wb') as f7:
                                        f0.write(first_q)
                                        f1.write(second_q)
                                        f2.write(third_q)
                                        f3.write(forth_q)
                                        f4.write(fifth_q)
                                        f5.write(sixth_q)
                                        f6.write(seventh_q)
                                        f7.write(seventh_q)

    chunks_write(tmp0, tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7, tmp8, header, out_path, temp_path, temp0_path)

number += 1
image_path = 'gingerbread.3dst'
yaxis_flip_3dst(image_path)
