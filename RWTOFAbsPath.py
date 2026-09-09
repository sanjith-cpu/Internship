txt_data = "I like Tofu!"
file_path = "C:/Users/s9ure/OneDrive/Desktop/output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")