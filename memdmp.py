def read_data_from_offset(filename, offset): # Just an example of what is in m3dsflip.py
    data_list = []
    with open(filename, 'rb') as file:
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
    filename = "gingerbread.3dst"
    offset = 0x20
    
    # Read data from the file starting from the offset
    data_blocks = read_data_from_offset(filename, offset)
    
    # Store each 16-byte block in separate variables
    num_blocks = len(data_blocks)
    for i, data_block in enumerate(data_blocks):
        var_name = f"data_block_{i}"
        print(var_name)
        globals()[var_name] = data_block

        
    with open(filename, 'rb') as file:
        header = file.read(offset)

    with open("generated_gingerbread.3dst", 'wb') as file0:
        file0.write(header)

        for i in range(1024):
            number0 = 1023 - i

            var_name = f"data_block_{number0}"
            data_block = globals()[var_name]

            # Write the data_block to the file
            file0.write(data_block)
