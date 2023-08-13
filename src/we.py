def split_file(filename, chunk_size):
    offset = 0x20  # Offset in bytes
    num_parts = 8
    
    with open(filename, "rb") as file:
        file.seek(offset)
        data = file.read()
    
    total_size = len(data)
    part_size = chunk_size * num_parts
    
    if total_size < part_size:
        print("File size is too small to create 8 parts.")
        return
    
    for i in range(num_parts):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        part_data = data[start:end]
        
        part_filename = f"temp{i + 1}.tempdata"
        with open(part_filename, "wb") as part_file:
            part_file.write(part_data)
        print(f"Part {i + 1} written to {part_filename}")

    print("File split into parts successfully.")

# Call the function with the desired filename and chunk size
split_file("gingy.3dst", 2048)