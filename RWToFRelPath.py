txt_data = "I like PaneerTofu!"
txt_data1 = "appended I like MushroomPaneerTofu!"
file_path = "Output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

    with open(file_path, "a") as file:
        file.write(txt_data1)
        print(f"txt file '{file_path}' was created")